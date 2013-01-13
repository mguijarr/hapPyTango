
=============================================================

hapPyTango depends on Python (< 3), gevent 1.0 (>= RC2)
and Fnorb (>= 1.3).

You can download gevent from here:
https://github.com/SiteSupport/gevent/downloads

And you can get Fnorb from the project SourceForge web page:
http://sourceforge.net/projects/fnorb/files/latest/download

How to install ?
----------------

Once dependencies are satisfied:
python setup.py install

What is it ?
------------

hapPyTango started as a fun week-end project, to have an
alternative Tango client library for Python that would be
lightweight, easy to install (especially on Windows! No
compilation, no C++ library needed), easy to use and
Pythonic, and that would take advantage of gevent.

Communication is handled by gevent coroutines, thus I/O operations
are non-blocking and any host application running the gevent loop
can benefit from asynchronous communication with Tango devices.
Using a dedicated input hook for IPython, for example, it becomes
easy to write complex sequences involving Tango devices taking
advantage of cooperative multi-tasking.

Old-style events (with notifd) does *not* work. Support was
planned initially, but due to some weird error in CDR
decoding, it has been dropped.
New style events (with zmq) will be implemented in a future
version when stable ZMQ library v3.2 will provide backward
compatibility with ZMQ 3.1.

The code is less than 500 lines. Of course it is far from being
a complete Tango client like PyTango, the official Tango client
for Python.

How to use it ?
---------------

<pre>
Python 2.6.5 (r265:79063, Oct  1 2012, 22:07:21) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from hapPyTango import client
>>> dev = client.Device("sys/tg_test/1")
>>> dir(dev)
['DevBoolean', 'DevDouble', 'DevFloat', 'DevLong', 'DevShort', 'DevString', 'DevULong', 'DevUShort', 'DevVarCharArray', 'DevVarDoubleArray', 'DevVarDoubleStringArray', 'DevVarFloatArray', 'DevVarLongArray', 'DevVarLongStringArray', 'DevVarShortArray', 'DevVarStringArray', 'DevVarULongArray', 'DevVarUShortArray', 'DevVoid', 'Init', 'State', 'Status', 'SwitchStates', '__doc__', '__init__', '__module__', '_attributes', '_boa', '_commands', '_connection_greenlet', '_db_host', '_device', '_device_impl_number', '_do_connect_event', '_ev_channel', '_keepalive_greenlet', '_nodb_flag', '_orb', '_tango_db', 'ampli', 'boolean_image', 'boolean_image_ro', 'boolean_scalar', 'boolean_spectrum', 'boolean_spectrum_ro', 'cmd_inout', 'connect', 'connect_event', 'double_image', 'double_image_ro', 'double_scalar', 'double_scalar_rww', 'double_scalar_w', 'double_spectrum', 'double_spectrum_ro', 'float_image', 'float_image_ro', 'float_scalar', 'float_spectrum', 'float_spectrum_ro', 'impl', 'init', 'initialized_event', 'long_image', 'long_image_ro', 'long_scalar', 'long_scalar_rww', 'long_scalar_w', 'long_spectrum', 'long_spectrum_ro', 'name', 'no_value', 'ping', 'read_attr', 'short_image', 'short_image_ro', 'short_scalar', 'short_scalar_ro', 'short_scalar_rww', 'short_scalar_w', 'short_spectrum', 'short_spectrum_ro', 'string_image', 'string_image_ro', 'string_scalar', 'string_spectrum', 'string_spectrum_ro', 'throw_exception', 'uchar_image', 'uchar_image_ro', 'uchar_scalar', 'uchar_spectrum', 'uchar_spectrum_ro', 'ushort_image', 'ushort_image_ro', 'ushort_scalar', 'ushort_spectrum', 'ushort_spectrum_ro', 'wait_initialized', 'wave', 'write_attr']
</pre>

Attributes are read and written like Commands.

When calling a command (or reading/writing an attribute), the
"wait" keyword argument allows to specify if the behaviour should
be synchronous (wait=True, default) or asynchronous (wait=False).
In the asynchronous case, a greenlet object is returned. Doing get()
on this object to wait for completion and getting the result (for
more options, see gevent documentation).

Other keyword arguments can be passed: "timeout" allows to specify
a timeout in seconds (default: 3 seconds), "from_cache" specifies if
values should be returned from cache or from device (default: from
device). For arguments reading:
- "return_value" indicates if the attribute value should be returned, 
or the complete attribute_value object (default: True)
- "return_set_value" indicates if the set value has to be returned
too (default: False)

hapPyTango + IPython
--------------------

It is fairly easy to add an input hook to IPython to run gevent loop,
just as it is done for GUI loops for example: see the ipython.py module.
When starting IPython, make sure "enable_gevent_hook" is called:

start_ipython.sh

    #!/usr/bin/env python
    from IPython.frontend.terminal.interactiveshell import TerminalInteractiveShell
    from hapPyTango.client import Device 
    from hapPyTango.ipython import enable_gevent_hook

    shell = TerminalInteractiveShell(user_ns={"TangoDevice": Device, "gevent": gevent})

    enable_gevent_hook()

    shell.mainloop() 

Enjoy smooth integration of IPython, Tango and gevent :)



