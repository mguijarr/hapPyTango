""" Module: IDL:omg.org/CosNotification:1.0

Automagically generated by:-

The ORB called Fnorb v1.1.Return.of.Fnorb

"""

_FNORB_ID = "IDL:omg.org/CosNotification:1.0"

# Fnorb modules.
import Fnorb.orb.CORBA
import Fnorb.orb.TypeManager
import Fnorb.orb.Util

class QoSAdmin_skel(Fnorb.orb.CORBA.Object_skel):
    """ Interface: IDL:omg.org/CosNotification/QoSAdmin:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotification/QoSAdmin:1.0"

    def _skel_get_qos(self, server_request):
        """ Operation: IDL:omg.org/CosNotification/QoSAdmin/get_qos:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/QoSProperties:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.get_qos, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_set_qos(self, server_request):
        """ Operation: IDL:omg.org/CosNotification/QoSAdmin/set_qos:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/QoSProperties:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/UnsupportedQoS:1.0"))

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # Unmarshal the arguments to the request.
        arguments = server_request.arguments()

        # Invoke the implementation.
        results = apply(self.set_qos, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_validate_qos(self, server_request):
        """ Operation: IDL:omg.org/CosNotification/QoSAdmin/validate_qos:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/QoSProperties:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/NamedPropertyRangeSeq:1.0"))

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/UnsupportedQoS:1.0"))

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # Unmarshal the arguments to the request.
        arguments = server_request.arguments()

        # Invoke the implementation.
        results = apply(self.validate_qos, arguments)

        # Create the reply.
        server_request.results(results)

        return

class AdminPropertiesAdmin_skel(Fnorb.orb.CORBA.Object_skel):
    """ Interface: IDL:omg.org/CosNotification/AdminPropertiesAdmin:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotification/AdminPropertiesAdmin:1.0"

    def _skel_get_admin(self, server_request):
        """ Operation: IDL:omg.org/CosNotification/AdminPropertiesAdmin/get_admin:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/AdminProperties:1.0"))

        # Typecodes for user exceptions.
        exceptions = []

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # This operation has no arguments.
        arguments = ()

        # Invoke the implementation.
        results = apply(self.get_admin, arguments)

        # Create the reply.
        server_request.results(results)

        return

    def _skel_set_admin(self, server_request):
        """ Operation: IDL:omg.org/CosNotification/AdminPropertiesAdmin/set_admin:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/AdminProperties:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/UnsupportedAdmin:1.0"))

        # Initialise the server request object.
        server_request.initialise(inputs, outputs, exceptions)

        # Unmarshal the arguments to the request.
        arguments = server_request.arguments()

        # Invoke the implementation.
        results = apply(self.set_admin, arguments)

        # Create the reply.
        server_request.results(results)

        return

#############################################################################