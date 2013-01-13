import os
import sys
import types
import logging
import traceback
import weakref
import time
import gevent
import Tango
import AttNotification
import CosNotifyChannelAdmin
import CosNotification
import CosNotifyFilter
import CosNotifyComm_skel
from Fnorb.orb import CORBA
from Fnorb.orb import BOA


CONNECTION_TIMEOUT = 3
CALL_TIMEOUT = 1


def tango2python(v, scalar=False):
  #print v, v.value, v.__class__
  if isinstance(v, CORBA.Any):
    value = v.value()
    if isinstance(value, Tango.DevVarLongStringArray):
      return (value.lvalue, value.svalue)
    elif isinstance(value, Tango.DevVarDoubleStringArray):
      return (value.dvalue, value.svalue)
    else:
      if type(value)==types.ListType and scalar:
        # why is this happening???
        return value[0]
      else:
        return value
  else:
    return v


attrTypeEnum2str = { Tango.ATT_DOUBLE: ("DevDouble", "DevVarDoubleArray"),
                 Tango.ATT_STRING: ("DevString", "DevVarStringArray"),
                 Tango.ATT_BOOL: ("DevBoolean", "DevVarBooleanArray"),
                 Tango.ATT_SHORT: ("DevShort","DevVarShortArray"),
                 3: ("DevLong", "DevVarLongArray") }


typeEnum2str = { 0: ("DevVoid", ""),
                 1: ("DevBoolean", "DevVarBooleanArray"),
                 2: ("DevShort", "DevVarShortArray"),
                 3: ("DevLong", "DevVarLongArray"),
                 4: ("DevFloat", "DevVarFloatArray"),
                 5: ("DevDouble", "DevVarDoubleArray"),
                 6: ("DevUShort", "DevVarUShortArray"),
                 7: ("DevULong", "DevVarULongArray"), 
                 8: ("DevString", "DevVarStringArray"),
                 9: ("DevVarCharArray", None),
                 11: ("DevVarLongArray", None),
                 10: ("DevVarShortArray", None),
                 12: ("DevVarFloatArray", None),
                 13: ("DevVarDoubleArray", None),
                 14: ("DevVarUShortArray", None),
                 15: ("DevVarULongArray", None),
                 16: ("DevVarStringArray", None),
                 17: ("DevVarLongStringArray", None),
                 18: ("DevVarDoubleStringArray", None),
               }


def python2any(data, data_type=None, force_array=False, attr=False):
  if attr:
    typeEnum2str = globals()["attrTypeEnum2str"]
  else:
    typeEnum2str = globals()["typeEnum2str"]

  data_type_name, array_data_type_name = typeEnum2str[data_type]

  if data_type_name == "DevVarDoubleStringArray":
    # data is supposed to be a tuple with a list of doubles and a list of strings
    data = { "dvalue": data[0], "svalue": data[1] }
  elif data_type_name == "DevVarLongStringArray":
    # data is supposed to be a tuple with a list of longs and a list of strings
    data = { "lvalue": data[0], "svalue": data[1] }

  if force_array:
    data_type_name = array_data_type_name
    data = [data]

  return CORBA.Any(CORBA.typecode("IDL:Tango/%s:1.0" % data_type_name), data)


def do_tango_cmd_call(name, cmd_type, cmd_call, argin, source_type, wait, timeout, parent_proxy=None):
  with gevent.Timeout(timeout):
      try:
          if cmd_type is None:
            # special command like "status", "state"
            res = cmd_call()
          else:
            res = cmd_call(name, argin, source_type)
      except Tango.MultiDevFailed, e:
          raise RuntimeError(e.errors[0].err_list[0].desc)
      except Tango.DevFailed, e:
          raise RuntimeError(e.errors[0].desc)
      except: 
          if parent_proxy:
              parent_proxy.connect()
              cmd_call = getattr(parent_proxy, name).cmd_call
              return do_tango_cmd_call(name, cmd_type, cmd_call, argin, source_type, wait, timeout)
          raise RuntimeError

      return tango2python(res)


class tango_cmd_call:
  def __init__(self, device, cmd_name, cmd_type, cmd_call):
    if isinstance(device, Device):
        self.device = device._device
        self.proxy = device
    else:
        self.device = device
        self.proxy = None
    self.name = cmd_name
    self.cmd_type = cmd_type
    self.cmd_call = getattr(self.device, cmd_call) 

  def __call__(self, *args, **kwargs):
    timeout = kwargs.get("timeout", CALL_TIMEOUT)
    wait = kwargs.get("wait", True)
    from_cache = kwargs.get("from_cache", False)
    if from_cache:
      # CACHE_DEV
      source_type = Tango.DevSource[2]
    else:
      # DEV
      source_type = Tango.DevSource[0]

    if not args:
      argin = CORBA.Any(CORBA.NullTypeCode(), None)
    else:
      argin = python2any(args[0], self.cmd_type)

    # timeout is only took into account when we wait for result
    tango_call_greenlet = gevent.spawn(do_tango_cmd_call, 
                                       self.name, 
                                       self.cmd_type, 
                                       self.cmd_call, 
                                       argin, 
                                       source_type, 
                                       wait, 
                                       timeout if wait else None,
                                       parent_proxy = self.proxy)

    if wait:
      return tango_call_greenlet.get()
    else:
      return tango_call_greenlet


def do_tango_write_attr(device, name, write_attr_cmd_string, new_value, quality, timeout, parent_proxy=None):
    with gevent.Timeout(timeout):
      # get attribute cfg to have attr. type and dims
      try:
        attr_cfg = device.get_attribute_config([name])[0]
      except:
        if parent_proxy:
          parent_proxy.connect()
          device = parent_proxy._device
          return do_tango_write_attr(device, name, write_attr_cmd_string, new_value, quality, timeout)

      write_attr_cmd = getattr(device, write_attr_cmd_string)      

      try:
        # weird: even for single values, the data type has to be an array!!!
        write_attr_cmd([Tango.AttributeValue(python2any(new_value, attr_cfg.data_type, force_array=True, attr=True), 
                        quality, 
                        Tango.TimeVal(int(time.time()),0,0), 
                        name, 
                        attr_cfg.max_dim_x, 
                        attr_cfg.max_dim_y)])
      except Tango.MultiDevFailed, e:
        raise RuntimeError(e.errors[0].err_list[0].desc)
      except Tango.DevFailed, e:
        raise RuntimeError(e.errors[0].desc)
      #except:
      #  if parent_proxy:
      #    parent_proxy.connect()
      #    device = parent_proxy._device 
      #    return do_tango_write_attr(device, name, write_attr_cmd_string, new_value, quality, timeout)
      #  raise RuntimeError


def do_tango_read_attr(name, read_attr_cmd, source_type, timeout, parent_proxy=None):
  with gevent.Timeout(timeout):
      try:
        try:
          attribute_value_obj = read_attr_cmd([name], source_type)[0]
        except TypeError:
          attribute_value_obj = read_attr_cmd([name])[0]
      except Tango.MultiDevFailed, e:
        raise RuntimeError(e.errors[0].err_list[0].desc)
      except Tango.DevFailed, e:
        raise RuntimeError(e.errors[0].desc)
      except:
        if parent_proxy:
          parent_proxy.connect()
          read_attr_cmd = getattr(parent_proxy, name).read_attr_cmd
          attribute_value_obj = do_tango_read_attr(name, read_attr_cmd, source_type, timeout)
        else:
          raise RuntimeError
  return attribute_value_obj


class tango_attr_set_or_get:
  def __init__(self, device, attr_name, read_attr_cmd, write_attr_cmd, scalar=False):
    if isinstance(device, Device):
        self.device = device._device
        self.proxy = device
    else:
        self.device = device
        self.proxy = None
    self.name = attr_name
    self.timeout = None
    self.read_attr_cmd = getattr(self.device, read_attr_cmd)
    self.write_attr_cmd = write_attr_cmd 
    self.scalar = scalar

  def get_attr(self, from_cache=False, return_value=True, return_set_value=False):
    if from_cache:
      # CACHE_DEV
      source_type = Tango.DevSource[2]
    else:
      # DEV
      source_type = Tango.DevSource[0]

    attribute_value_obj = do_tango_read_attr(self.name, self.read_attr_cmd, source_type, self.timeout, parent_proxy=self.proxy) 
    
    if hasattr(attribute_value_obj, "err_list") and attribute_value_obj.err_list:
      raise RuntimeError, "\n".join([err.desc for err in attribute_value_obj.err_list])

    if return_value:
      attr_value = tango2python(attribute_value_obj.value, self.scalar)
      try:
        read_value, set_value = attr_value
      except:
        read_value = attr_value
        set_value = None
      if return_set_value:
        return read_value, set_value
      else:
        return read_value
    else:
      return attribute_value_obj

  
  def __call__(self, *args, **kwargs):
      self.timeout = kwargs.get("timeout", CALL_TIMEOUT)
      wait = kwargs.get("wait", True)
 
      if args:
          quality = kwargs.get("quality", Tango.ATTR_VALID)
          tango_attr_greenlet = gevent.spawn(do_tango_write_attr,
                                             self.device,
                                             self.name, 
                                             self.write_attr_cmd, 
                                             args[0], 
                                             quality, 
                                             self.timeout if wait else None, 
                                             parent_proxy=self.proxy) 
      else:
          tango_attr_greenlet = gevent.spawn(self.get_attr, kwargs.get("from_cache", False), kwargs.get("return_value", True), kwargs.get("return_set_value", False))

      if wait:
          return tango_attr_greenlet.get()
      else:
          return tango_attr_greenlet


"""
class EventConsumer(CosNotifyComm_skel.StructuredPushConsumer_skel):
  def push_structured_event(self, event):
    #print event.header.fixed_header.event_type.type_name
    if isinstance(event, DSI.ServerRequest):
      # weird problem with recursive TypeCode
      arguments = []
      cursor = event._ServerRequest__cursor
      for tc in event._ServerRequest__inputs:
          import pdb;pdb.set_trace()
          try:
            arguments.append(tc._fnorb_unmarshal_value(cursor))
          except:
            arguments.append(None)
      print arguments
      event=None 
    if event is None:
      print "bad event"
      return
    value = tango2python(event.remainder_of_body)
    try:
      print value.value.value()[0] #, dir(value.value)
    except:
      pass

  def disconnect_structured_push_consumer(self, server_req):
    pass 
"""

def get_device_ior(orb, tango_db, name, nodb):
    if nodb:
        device_ior = "corbaloc:iiop:%s/%s" % (tango_db, name)
        device_impl_number = 2 # all devices should be 2 at least... How to know which impl is the more suitable one?
        #device_host = tango_db.split(":")[0]
        logging.debug("direct connection to %s running @ %s", name, tango_db)
    else:
        logging.debug("connecting to %s using tango db %s", name, tango_db)

        obj = orb.string_to_object("corbaloc:iiop:%s/database" % tango_db)

        tango_db = obj._narrow(Tango.Device_3)

        _, res = tango_cmd_call(tango_db, "DbImportDevice", 8, "command_inout_2")(name)

        device_ior = res[1]
        device_impl_number = int(res[2])
        #device_host = res[4]
    return tango_db, device_ior, device_impl_number


def connect_device(tango_db, name, nodb=False): #, device_impl_number):
  while True:
    try:
      orb = CORBA.ORB_init(["--ORBthreading-model=Threaded"])
      tango_db_dev, device_ior, device_impl_number = get_device_ior(orb, tango_db, name, nodb)
      device_impl = Device.impl[device_impl_number]
      device = orb.string_to_object(device_ior)._narrow(device_impl)
      device.ping()
    except:
      time.sleep(CALL_TIMEOUT)
      continue
    else:
      return orb, tango_db_dev, device, device_impl_number


def keepalive_ping(device_ref):
  time.sleep(3)
  while True:
    device_proxy = device_ref()
    if device_proxy is None:
      return
    try:
      device_proxy._device.ping()
    except:   
      return
    del device_proxy
    time.sleep(3)


class Device:
  impl = [None, Tango.Device, Tango.Device_2, Tango.Device_3, Tango.Device_3]
  cmd_inout = [None, "command_inout", "command_inout_2", "command_inout_2", "command_inout_2"] #"command_inout_4"] #don't use this command because don't know what ClntIdent is
  read_attr = [None, "read_attributes", "read_attributes_2", "read_attributes_3", "read_attributes_3"] #"read_attributes_4"] 
  write_attr = [None, "write_attributes", "write_attributes", "write_attributes_3", "write_attributes_3"]

  def __init__(self, device_name, timeout=CONNECTION_TIMEOUT):
    self._db_host = None
    self._nodb_flag = False
    self._tango_db = None
    self._device = None
    self._device_impl_number = None
    self._ev_channel = None
    self._connection_greenlet = None
    self._keepalive_greenlet = None
    self._orb = None
    self._boa = None

    # have to get tango_db from device name or environment variable
    # also, find if we should use database to connect to device or not
    try:
      tango_db = device_name.replace("tango://", "")

      tango_db, domain, family, name = tango_db.split("/")

      self.name = "/".join([domain, family, name])
    except:
      tango_db = os.environ["TANGO_HOST"]
      self.name = device_name
    else:
      self._nodb_flag = device_name.endswith("#dbase=no")
      self.name = self.name.replace("#dbase=no", "")

    self._db_host = tango_db

    self.connect(timeout) 


  def connect(self, timeout=CONNECTION_TIMEOUT): 
    try:
        self.ping()
    except:
        try:
          self._connection_greenlet.kill()
        except: 
          pass
        self._connection_greenlet = None
    else:
        return

    if not self._connection_greenlet: 
      try:
        self._keepalive_greenlet.kill()
      except:
        pass
      self._connection_greenlet = gevent.spawn(connect_device, self._db_host, self.name, self._nodb_flag)
  
    if timeout <= 0:
        return

    self.wait_initialized(timeout)


  def wait_initialized(self, timeout=CONNECTION_TIMEOUT):
    with gevent.Timeout(timeout, RuntimeError("Device %s is not exported" % self.name)):
      try:
          self._orb, self._tango_db, self._device, self._device_impl_number = self._connection_greenlet.get()
      except gevent.Timeout:
          raise RuntimeError("Device %s is not exported" % self.name)
      else:
        return self.init()


  def init(self): #, connection_greenlet):
    """Finish proxy initialization, fills in attributes and commands"""
    self._keepalive_greenlet = gevent.spawn(keepalive_ping, weakref.ref(self))
 
    # do command list query on device and create commands as methods
    for cmd in self._device.command_list_query():
      setattr(self, cmd.cmd_name, tango_cmd_call(self, cmd.cmd_name, cmd.in_type, Device.cmd_inout[self._device_impl_number]))

    # each attribute will be converted into a method too
    # the way to get attributes list is weird 
    if self._device_impl_number < 3:
      attributes_list = self._device.get_attribute_config(["All attributes"])
    else:
      attributes_list = self._device.get_attribute_config(["All attributes_3"])
    for attr in attributes_list:
      setattr(self, attr.name, tango_attr_set_or_get(self, attr.name, Device.read_attr[self._device_impl_number], Device.write_attr[self._device_impl_number], str(attr.data_format)=="SCALAR"))

    if not hasattr(self, "Status"):
      # State and Status are special
      setattr(self, "Status", tango_cmd_call(self, "Status", None, "_get_status"))
      setattr(self, "State", tango_cmd_call(self, "State", None, "_get_state"))


  def ping(self):
    return self._device.ping()


  """
  def connect_event(self, attribute_name, callback):
    self._event_consumer = EventConsumer()
    if not self._boa:
      self._boa = BOA.BOA_init()
      self._event_loop = None
    ref = self._boa.create(str(id(self._event_consumer)), self._event_consumer._FNORB_ID)
    self._boa.obj_is_ready(ref, self._event_consumer)

    self._do_connect_event(attribute_name, callback, None)

    if not self._event_loop:
      self._event_loop = gevent.spawn(self._boa._fnorb_mainloop)


  def _do_connect_event(self, attribute_name, callback, event_consumer):
    res = tango_cmd_call(self._tango_db, "DbImportEvent", 8, "command_inout_2")(self._device._get_adm_name())
    print res
    if len(res) == 2:
      ev_channel_ior = res[1][1]
    else:  
      ev_channel_ior = res[1]

    try:
      self._ev_channel = self._orb.string_to_object(ev_channel_ior)._narrow(AttNotification.EventChannel) 
    except:
      raise RuntimeError, "failed to narrow EventChannel - hint: is notifd running on host?"

    adm_device_proxy = Device(self._db_host+"/"+self._device._get_adm_name())

    adm_device_proxy.EventSubscriptionChange([self.name, attribute_name.lower(), "subscribe", "change"])

    # build a filter
    #ff = self._ev_channel._get_default_filter_factory()._narrow(AttNotification.FilterFactory)
    #filterobj = ff.create_filter("EXTENDED_TCL")
    #filterobj._narrow(AttNotification.Filter)
    #filterobj.add_constraints([CosNotifyFilter.ConstraintExp([CosNotification.EventType(self.name+"/"+attribute_name.lower(), "change")], "$name == 'heartbeat_counter'")])
    consumer_admin = self._ev_channel._get_default_consumer_admin()
    consumer_admin._narrow(AttNotification.ConsumerAdmin)
    
    proxy_push_supplier, proxy_id = consumer_admin.obtain_notification_push_supplier(CosNotifyChannelAdmin.STRUCTURED_EVENT)
    proxy_push_supplier._narrow(AttNotification.ProxyPushSupplier)

    proxy_push_supplier.connect_structured_push_consumer(self._event_consumer)
  """
