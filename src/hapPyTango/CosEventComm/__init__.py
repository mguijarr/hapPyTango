""" Module: IDL:omg.org/CosEventComm:1.0

Automagically generated by:-

The ORB called Fnorb v1.1.Return.of.Fnorb

"""

_FNORB_ID = "IDL:omg.org/CosEventComm:1.0"

# Fnorb modules.
import Fnorb.orb.CORBA
import Fnorb.orb.TypeManager
import Fnorb.orb.Util

class Disconnected(Fnorb.orb.CORBA.UserException):
    """ Exception: IDL:omg.org/CosEventComm/Disconnected:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventComm/Disconnected:1.0"

    def __init__(self):
        """ Constructor. """

        return

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventComm/Disconnected:1.0", "00000000000000160000004C000000000000002A49444C3A6F6D672E6F72672F436F734576656E74436F6D6D2F446973636F6E6E65637465643A312E300000000000000D446973636F6E6E65637465640000000000000000", Disconnected)

class PushConsumer(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosEventComm/PushConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventComm/PushConsumer:1.0"

    def push(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventComm/PushConsumer/push:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_any)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("push", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def disconnect_push_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventComm/PushConsumer/disconnect_push_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_push_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventComm/PushConsumer:1.0", "000000000000000E00000045000000000000002A49444C3A6F6D672E6F72672F436F734576656E74436F6D6D2F50757368436F6E73756D65723A312E300000000000000D50757368436F6E73756D657200", PushConsumer)

class PushSupplier(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosEventComm/PushSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventComm/PushSupplier:1.0"

    def disconnect_push_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventComm/PushSupplier/disconnect_push_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_push_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventComm/PushSupplier:1.0", "000000000000000E00000045000000000000002A49444C3A6F6D672E6F72672F436F734576656E74436F6D6D2F50757368537570706C6965723A312E300000000000000D50757368537570706C69657200", PushSupplier)

class PullSupplier(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosEventComm/PullSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventComm/PullSupplier:1.0"

    def pull(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventComm/PullSupplier/pull:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_any)

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("pull", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def try_pull(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventComm/PullSupplier/try_pull:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.TC_any)
        outputs.append(Fnorb.orb.CORBA.TC_boolean)

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("try_pull", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def disconnect_pull_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventComm/PullSupplier/disconnect_pull_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_pull_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventComm/PullSupplier:1.0", "000000000000000E00000045000000000000002A49444C3A6F6D672E6F72672F436F734576656E74436F6D6D2F50756C6C537570706C6965723A312E300000000000000D50756C6C537570706C69657200", PullSupplier)

class PullConsumer(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosEventComm/PullConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosEventComm/PullConsumer:1.0"

    def disconnect_pull_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosEventComm/PullConsumer/disconnect_pull_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_pull_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosEventComm/PullConsumer:1.0", "000000000000000E00000045000000000000002A49444C3A6F6D672E6F72672F436F734576656E74436F6D6D2F50756C6C436F6E73756D65723A312E300000000000000D50756C6C436F6E73756D657200", PullConsumer)

#############################################################################
