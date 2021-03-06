""" Module: IDL:omg.org/CosEventChannelAdmin:1.0

Automagically generated by:-

The ORB called Fnorb v1.1.Return.of.Fnorb

"""

_FNORB_ID = "IDL:omg.org/CosEventChannelAdmin:1.0"

# Fnorb modules.
import Fnorb.orb.CORBA
import Fnorb.orb.TypeManager
import Fnorb.orb.Util

class AlreadyConnected(Fnorb.orb.CORBA.UserException):
    """ Exception: IDL:omg.org/CosEventChannelAdmin/AlreadyConnected:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/AlreadyConnected:1.0"

    def __init__(self):
        """ Constructor. """

        return

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/AlreadyConnected:1.0", "00000000000000160000005C000000000000003649444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F416C7265616479436F6E6E65637465643A312E3000000000000011416C7265616479436F6E6E65637465640000000000000000", AlreadyConnected)

class TypeError(Fnorb.orb.CORBA.UserException):
    """ Exception: IDL:omg.org/CosEventChannelAdmin/TypeError:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/TypeError:1.0"

    def __init__(self):
        """ Constructor. """

        return

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/TypeError:1.0", "00000000000000160000004C000000000000002F49444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F547970654572726F723A312E3000000000000A547970654572726F7200000000000000", TypeError)

# Import base interface packages.
import CosEventComm

class ProxyPushConsumer(Fnorb.orb.CORBA.Object, CosEventComm.PushConsumer):
    """ Interface: IDL:omg.org/CosEventChannelAdmin/ProxyPushConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/ProxyPushConsumer:1.0"

    def connect_push_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/ProxyPushConsumer/connect_push_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventChannelAdmin/AlreadyConnected:1.0"))

        # Create a request object.
        request = self._create_request("connect_push_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/ProxyPushConsumer:1.0", "000000000000000E00000056000000000000003749444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F50726F787950757368436F6E73756D65723A312E3000000000001250726F787950757368436F6E73756D657200", ProxyPushConsumer)

# Import base interface packages.
import CosEventComm

class ProxyPullSupplier(Fnorb.orb.CORBA.Object, CosEventComm.PullSupplier):
    """ Interface: IDL:omg.org/CosEventChannelAdmin/ProxyPullSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/ProxyPullSupplier:1.0"

    def connect_pull_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/ProxyPullSupplier/connect_pull_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventChannelAdmin/AlreadyConnected:1.0"))

        # Create a request object.
        request = self._create_request("connect_pull_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/ProxyPullSupplier:1.0", "000000000000000E00000056000000000000003749444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F50726F787950756C6C537570706C6965723A312E3000000000001250726F787950756C6C537570706C69657200", ProxyPullSupplier)

# Import base interface packages.
import CosEventComm

class ProxyPullConsumer(Fnorb.orb.CORBA.Object, CosEventComm.PullConsumer):
    """ Interface: IDL:omg.org/CosEventChannelAdmin/ProxyPullConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/ProxyPullConsumer:1.0"

    def connect_pull_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/ProxyPullConsumer/connect_pull_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventChannelAdmin/AlreadyConnected:1.0"))
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventChannelAdmin/TypeError:1.0"))

        # Create a request object.
        request = self._create_request("connect_pull_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/ProxyPullConsumer:1.0", "000000000000000E00000056000000000000003749444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F50726F787950756C6C436F6E73756D65723A312E3000000000001250726F787950756C6C436F6E73756D657200", ProxyPullConsumer)

# Import base interface packages.
import CosEventComm

class ProxyPushSupplier(Fnorb.orb.CORBA.Object, CosEventComm.PushSupplier):
    """ Interface: IDL:omg.org/CosEventChannelAdmin/ProxyPushSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/ProxyPushSupplier:1.0"

    def connect_push_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/ProxyPushSupplier/connect_push_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventChannelAdmin/AlreadyConnected:1.0"))
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventChannelAdmin/TypeError:1.0"))

        # Create a request object.
        request = self._create_request("connect_push_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/ProxyPushSupplier:1.0", "000000000000000E00000056000000000000003749444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F50726F787950757368537570706C6965723A312E3000000000001250726F787950757368537570706C69657200", ProxyPushSupplier)

class ConsumerAdmin(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosEventChannelAdmin/ConsumerAdmin:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/ConsumerAdmin:1.0"

    def obtain_push_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/ConsumerAdmin/obtain_push_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("obtain_push_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def obtain_pull_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/ConsumerAdmin/obtain_pull_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("obtain_pull_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/ConsumerAdmin:1.0", "000000000000000E0000004E000000000000003349444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F436F6E73756D657241646D696E3A312E3000000000000E436F6E73756D657241646D696E00", ConsumerAdmin)

class SupplierAdmin(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosEventChannelAdmin/SupplierAdmin:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/SupplierAdmin:1.0"

    def obtain_push_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/SupplierAdmin/obtain_push_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("obtain_push_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def obtain_pull_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/SupplierAdmin/obtain_pull_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("obtain_pull_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/SupplierAdmin:1.0", "000000000000000E0000004E000000000000003349444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F537570706C69657241646D696E3A312E3000000000000E537570706C69657241646D696E00", SupplierAdmin)

class EventChannel(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosEventChannelAdmin/EventChannel:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventChannelAdmin/EventChannel:1.0"

    def for_consumers(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/EventChannel/for_consumers:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("for_consumers", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def for_suppliers(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/EventChannel/for_suppliers:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("for_suppliers", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def destroy(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventChannelAdmin/EventChannel/destroy:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("destroy", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventChannelAdmin/EventChannel:1.0", "000000000000000E0000004D000000000000003249444C3A6F6D672E6F72672F436F734576656E744368616E6E656C41646D696E2F4576656E744368616E6E656C3A312E300000000000000D4576656E744368616E6E656C00", EventChannel)

#############################################################################
