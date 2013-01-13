""" Module: IDL:att.com/AttNotification:1.0

Automagically generated by:-

The ORB called Fnorb v1.1.Return.of.Fnorb

"""

_FNORB_ID = "IDL:att.com/AttNotification:1.0"

# Fnorb modules.
import Fnorb.orb.CORBA
import Fnorb.orb.TypeManager
import Fnorb.orb.Util

class Interactive_skel(Fnorb.orb.CORBA.Object_skel):
    """ Interface: IDL:att.com/AttNotification/Interactive:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/Interactive:1.0"

    def _skel_do_command(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Interactive/do_command:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_string)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_string)
        outputs.append(Fnorb.orb.CORBA.TC_boolean)
        outputs.append(Fnorb.orb.CORBA.TC_boolean)
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # Unmarshal the arguments to the request.
        arguments = server_request.arguments()

        # Invoke the implementation.
        results = apply(self.do_command, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_my_name(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Interactive/my_name:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:att.com/AttNotification/NameSeq:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.my_name, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_child_names(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Interactive/child_names:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:att.com/AttNotification/NameSeq:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.child_names, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_children(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Interactive/children:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_boolean)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:att.com/AttNotification/IactSeq:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # Unmarshal the arguments to the request.
        arguments = server_request.arguments()

        # Invoke the implementation.
        results = apply(self.children, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_safe_cleanup(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Interactive/safe_cleanup:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_boolean)

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.safe_cleanup, arguments)

        # Create the reply.
        server_request.results(results)

        return

# Import base interface packages.
import CosEventChannelAdmin_skel

class CosEvProxyPushSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosEventChannelAdmin_skel.ProxyPushSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/CosEvProxyPushSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/CosEvProxyPushSupplier:1.0"

    pass

# Import base interface packages.
import CosEventChannelAdmin_skel

class CosEvProxyPullSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosEventChannelAdmin_skel.ProxyPullSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/CosEvProxyPullSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/CosEvProxyPullSupplier:1.0"

    pass

# Import base interface packages.
import CosEventChannelAdmin_skel

class CosEvProxyPushConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosEventChannelAdmin_skel.ProxyPushConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/CosEvProxyPushConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/CosEvProxyPushConsumer:1.0"

    pass

# Import base interface packages.
import CosEventChannelAdmin_skel

class CosEvProxyPullConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosEventChannelAdmin_skel.ProxyPullConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/CosEvProxyPullConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/CosEvProxyPullConsumer:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class ProxyPushSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.ProxyPushSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/ProxyPushSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/ProxyPushSupplier:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class ProxyPullSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.ProxyPullSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/ProxyPullSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/ProxyPullSupplier:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class ProxyPushConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.ProxyPushConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/ProxyPushConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/ProxyPushConsumer:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class ProxyPullConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.ProxyPullConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/ProxyPullConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/ProxyPullConsumer:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class StructuredProxyPushSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.StructuredProxyPushSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/StructuredProxyPushSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/StructuredProxyPushSupplier:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class StructuredProxyPullSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.StructuredProxyPullSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/StructuredProxyPullSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/StructuredProxyPullSupplier:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class StructuredProxyPushConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.StructuredProxyPushConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/StructuredProxyPushConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/StructuredProxyPushConsumer:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class StructuredProxyPullConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.StructuredProxyPullConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/StructuredProxyPullConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/StructuredProxyPullConsumer:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class SequenceProxyPushSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.SequenceProxyPushSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/SequenceProxyPushSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/SequenceProxyPushSupplier:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class SequenceProxyPullSupplier_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.SequenceProxyPullSupplier_skel):
    """ Interface: IDL:att.com/AttNotification/SequenceProxyPullSupplier:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/SequenceProxyPullSupplier:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class SequenceProxyPushConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.SequenceProxyPushConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/SequenceProxyPushConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/SequenceProxyPushConsumer:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class SequenceProxyPullConsumer_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.SequenceProxyPullConsumer_skel):
    """ Interface: IDL:att.com/AttNotification/SequenceProxyPullConsumer:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/SequenceProxyPullConsumer:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class SupplierAdmin_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.SupplierAdmin_skel):
    """ Interface: IDL:att.com/AttNotification/SupplierAdmin:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/SupplierAdmin:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class ConsumerAdmin_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.ConsumerAdmin_skel):
    """ Interface: IDL:att.com/AttNotification/ConsumerAdmin:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/ConsumerAdmin:1.0"

    pass

# Import base interface packages.
import CosNotifyChannelAdmin_skel

class EventChannel_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.EventChannel_skel):
    """ Interface: IDL:att.com/AttNotification/EventChannel:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/EventChannel:1.0"

    def _skel_obtain_subscription_types(self, server_request):
        """ Operation: IDL:att.com/AttNotification/EventChannel/obtain_subscription_types:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventTypeSeq:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.obtain_subscription_types, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_obtain_offered_types(self, server_request):
        """ Operation: IDL:att.com/AttNotification/EventChannel/obtain_offered_types:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventTypeSeq:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.obtain_offered_types, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_obtain_stats(self, server_request):
        """ Operation: IDL:att.com/AttNotification/EventChannel/obtain_stats:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:att.com/AttNotification/ChannelStats:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.obtain_stats, arguments)

        # Create the reply.
        server_request.results(results)

        return

# Import base interface packages.
import CosNotifyChannelAdmin_skel
import CosNotification_skel
import CosNotification_skel

class EventChannelFactory_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyChannelAdmin_skel.EventChannelFactory_skel, CosNotification_skel.QoSAdmin_skel, CosNotification_skel.AdminPropertiesAdmin_skel):
    """ Interface: IDL:att.com/AttNotification/EventChannelFactory:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/EventChannelFactory:1.0"

    pass

# Import base interface packages.
import CosNotifyFilter_skel

class Filter_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyFilter_skel.Filter_skel):
    """ Interface: IDL:att.com/AttNotification/Filter:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/Filter:1.0"

    def _skel_MyFID(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Filter/MyFID:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotifyFilter/FilterID:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.MyFID, arguments)

        # Create the reply.
        server_request.results(results)

        return

# Import base interface packages.
import CosNotifyFilter_skel

class MappingFilter_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyFilter_skel.MappingFilter_skel):
    """ Interface: IDL:att.com/AttNotification/MappingFilter:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/MappingFilter:1.0"

    pass

# Import base interface packages.
import CosNotifyFilter_skel

class FilterFactory_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel, CosNotifyFilter_skel.FilterFactory_skel):
    """ Interface: IDL:att.com/AttNotification/FilterFactory:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/FilterFactory:1.0"

    pass

class Server_skel(Fnorb.orb.CORBA.Object_skel, Interactive_skel):
    """ Interface: IDL:att.com/AttNotification/Server:1.0 """

    _FNORB_ID = "IDL:att.com/AttNotification/Server:1.0"

    def _skel_destroy(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Server/destroy:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.destroy, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_get_filter_factory(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Server/get_filter_factory:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.get_filter_factory, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_get_channel_factory(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Server/get_channel_factory:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.get_channel_factory, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_get_default_channel(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Server/get_default_channel:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_Object)

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.get_default_channel, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_results_to_file(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Server/results_to_file:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_boolean)

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.results_to_file, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_get_server_props(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Server/get_server_props:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:att.com/AttNotification/ServerProperties:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.get_server_props, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_set_server_props(self, server_request):
        """ Operation: IDL:att.com/AttNotification/Server/set_server_props:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:att.com/AttNotification/ServerProperties:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:att.com/AttNotification/UnsupportedServerProp:1.0"))

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # Unmarshal the arguments to the request.
        arguments = server_request.arguments()

        # Invoke the implementation.
        results = apply(self.set_server_props, arguments)

        # Create the reply.
        server_request.results(results)

        return

#############################################################################