""" Module: IDL:omg.org/CosNotifyComm:1.0

Automagically generated by:-

The ORB called Fnorb v1.1.Return.of.Fnorb

"""

_FNORB_ID = "IDL:omg.org/CosNotifyComm:1.0"

# Fnorb modules.
import Fnorb.orb.CORBA
import Fnorb.orb.TypeManager
import Fnorb.orb.Util

class InvalidEventType(Fnorb.orb.CORBA.UserException):
    """ Exception: IDL:omg.org/CosNotifyComm/InvalidEventType:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/InvalidEventType:1.0"

    def __init__(self, _type):
        """ Constructor. """

        self.type = _type
        return

    def __getinitargs__(self):
        """ Return the constructor arguments for unpickling. """

        return (self.type,)

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/InvalidEventType:1.0", "0000000000000016000000E0000000000000002F49444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F496E76616C69644576656E74547970653A312E30000000000011496E76616C69644576656E745479706500000000000000010000000574797065000000000000000F00000078000000000000002A49444C3A6F6D672E6F72672F436F734E6F74696669636174696F6E2F4576656E74547970653A312E300000000000000A4576656E7454797065000000000000020000000C646F6D61696E5F6E616D650000000012000000000000000A747970655F6E616D650000000000001200000000", InvalidEventType)

class NotifyPublish(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosNotifyComm/NotifyPublish:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/NotifyPublish:1.0"

    def offer_change(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/NotifyPublish/offer_change:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventTypeSeq:1.0"))
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventTypeSeq:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotifyComm/InvalidEventType:1.0"))

        # Create a request object.
        request = self._create_request("offer_change", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/NotifyPublish:1.0", "000000000000000E00000046000000000000002C49444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F4E6F746966795075626C6973683A312E30000000000E4E6F746966795075626C69736800", NotifyPublish)

class NotifySubscribe(Fnorb.orb.CORBA.Object):
    """ Interface: IDL:omg.org/CosNotifyComm/NotifySubscribe:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/NotifySubscribe:1.0"

    def subscription_change(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/NotifySubscribe/subscription_change:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventTypeSeq:1.0"))
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventTypeSeq:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotifyComm/InvalidEventType:1.0"))

        # Create a request object.
        request = self._create_request("subscription_change", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/NotifySubscribe:1.0", "000000000000000E0000004C000000000000002E49444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F4E6F746966795375627363726962653A312E30000000000000104E6F7469667953756273637269626500", NotifySubscribe)

# Import base interface packages.
import CosEventComm

class PushConsumer(Fnorb.orb.CORBA.Object, NotifyPublish, CosEventComm.PushConsumer):
    """ Interface: IDL:omg.org/CosNotifyComm/PushConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/PushConsumer:1.0"

    pass

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/PushConsumer:1.0", "000000000000000E00000045000000000000002B49444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F50757368436F6E73756D65723A312E3000000000000D50757368436F6E73756D657200", PushConsumer)

# Import base interface packages.
import CosEventComm

class PullConsumer(Fnorb.orb.CORBA.Object, NotifyPublish, CosEventComm.PullConsumer):
    """ Interface: IDL:omg.org/CosNotifyComm/PullConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/PullConsumer:1.0"

    pass

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/PullConsumer:1.0", "000000000000000E00000045000000000000002B49444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F50756C6C436F6E73756D65723A312E3000000000000D50756C6C436F6E73756D657200", PullConsumer)

# Import base interface packages.
import CosEventComm

class PullSupplier(Fnorb.orb.CORBA.Object, NotifySubscribe, CosEventComm.PullSupplier):
    """ Interface: IDL:omg.org/CosNotifyComm/PullSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/PullSupplier:1.0"

    pass

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/PullSupplier:1.0", "000000000000000E00000045000000000000002B49444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F50756C6C537570706C6965723A312E3000000000000D50756C6C537570706C69657200", PullSupplier)

# Import base interface packages.
import CosEventComm

class PushSupplier(Fnorb.orb.CORBA.Object, NotifySubscribe, CosEventComm.PushSupplier):
    """ Interface: IDL:omg.org/CosNotifyComm/PushSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/PushSupplier:1.0"

    pass

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/PushSupplier:1.0", "000000000000000E00000045000000000000002B49444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F50757368537570706C6965723A312E3000000000000D50757368537570706C69657200", PushSupplier)

class StructuredPushConsumer(Fnorb.orb.CORBA.Object, NotifyPublish):
    """ Interface: IDL:omg.org/CosNotifyComm/StructuredPushConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/StructuredPushConsumer:1.0"

    def push_structured_event(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/StructuredPushConsumer/push_structured_event:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/StructuredEvent:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("push_structured_event", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def disconnect_structured_push_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/StructuredPushConsumer/disconnect_structured_push_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_structured_push_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/StructuredPushConsumer:1.0", "000000000000000E0000005B000000000000003549444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F5374727563747572656450757368436F6E73756D65723A312E3000000000000000175374727563747572656450757368436F6E73756D657200", StructuredPushConsumer)

class StructuredPullConsumer(Fnorb.orb.CORBA.Object, NotifyPublish):
    """ Interface: IDL:omg.org/CosNotifyComm/StructuredPullConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/StructuredPullConsumer:1.0"

    def disconnect_structured_pull_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/StructuredPullConsumer/disconnect_structured_pull_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_structured_pull_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/StructuredPullConsumer:1.0", "000000000000000E0000005B000000000000003549444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F5374727563747572656450756C6C436F6E73756D65723A312E3000000000000000175374727563747572656450756C6C436F6E73756D657200", StructuredPullConsumer)

class StructuredPullSupplier(Fnorb.orb.CORBA.Object, NotifySubscribe):
    """ Interface: IDL:omg.org/CosNotifyComm/StructuredPullSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/StructuredPullSupplier:1.0"

    def pull_structured_event(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/StructuredPullSupplier/pull_structured_event:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/StructuredEvent:1.0"))

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("pull_structured_event", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def try_pull_structured_event(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/StructuredPullSupplier/try_pull_structured_event:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/StructuredEvent:1.0"))
        outputs.append(Fnorb.orb.CORBA.TC_boolean)

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("try_pull_structured_event", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def disconnect_structured_pull_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/StructuredPullSupplier/disconnect_structured_pull_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_structured_pull_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/StructuredPullSupplier:1.0", "000000000000000E0000005B000000000000003549444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F5374727563747572656450756C6C537570706C6965723A312E3000000000000000175374727563747572656450756C6C537570706C69657200", StructuredPullSupplier)

class StructuredPushSupplier(Fnorb.orb.CORBA.Object, NotifySubscribe):
    """ Interface: IDL:omg.org/CosNotifyComm/StructuredPushSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/StructuredPushSupplier:1.0"

    def disconnect_structured_push_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/StructuredPushSupplier/disconnect_structured_push_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_structured_push_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/StructuredPushSupplier:1.0", "000000000000000E0000005B000000000000003549444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F5374727563747572656450757368537570706C6965723A312E3000000000000000175374727563747572656450757368537570706C69657200", StructuredPushSupplier)

class SequencePushConsumer(Fnorb.orb.CORBA.Object, NotifyPublish):
    """ Interface: IDL:omg.org/CosNotifyComm/SequencePushConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/SequencePushConsumer:1.0"

    def push_structured_events(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/SequencePushConsumer/push_structured_events:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventBatch:1.0"))

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("push_structured_events", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def disconnect_sequence_push_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/SequencePushConsumer/disconnect_sequence_push_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_sequence_push_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/SequencePushConsumer:1.0", "000000000000000E00000055000000000000003349444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F53657175656E636550757368436F6E73756D65723A312E3000000000001553657175656E636550757368436F6E73756D657200", SequencePushConsumer)

class SequencePullConsumer(Fnorb.orb.CORBA.Object, NotifyPublish):
    """ Interface: IDL:omg.org/CosNotifyComm/SequencePullConsumer:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/SequencePullConsumer:1.0"

    def disconnect_sequence_pull_consumer(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/SequencePullConsumer/disconnect_sequence_pull_consumer:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_sequence_pull_consumer", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/SequencePullConsumer:1.0", "000000000000000E00000055000000000000003349444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F53657175656E636550756C6C436F6E73756D65723A312E3000000000001553657175656E636550756C6C436F6E73756D657200", SequencePullConsumer)

class SequencePullSupplier(Fnorb.orb.CORBA.Object, NotifySubscribe):
    """ Interface: IDL:omg.org/CosNotifyComm/SequencePullSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/SequencePullSupplier:1.0"

    def pull_structured_events(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/SequencePullSupplier/pull_structured_events:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_long)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventBatch:1.0"))

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("pull_structured_events", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def try_pull_structured_events(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/SequencePullSupplier/try_pull_structured_events:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []
        inputs.append(Fnorb.orb.CORBA.TC_long)

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []
        outputs.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosNotification/EventBatch:1.0"))
        outputs.append(Fnorb.orb.CORBA.TC_boolean)

        # Typecodes for user exceptions.
        exceptions = []
        exceptions.append(Fnorb.orb.CORBA.typecode("IDL:omg.org/CosEventComm/Disconnected:1.0"))

        # Create a request object.
        request = self._create_request("try_pull_structured_events", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

    def disconnect_sequence_pull_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/SequencePullSupplier/disconnect_sequence_pull_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_sequence_pull_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/SequencePullSupplier:1.0", "000000000000000E00000055000000000000003349444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F53657175656E636550756C6C537570706C6965723A312E3000000000001553657175656E636550756C6C537570706C69657200", SequencePullSupplier)

class SequencePushSupplier(Fnorb.orb.CORBA.Object, NotifySubscribe):
    """ Interface: IDL:omg.org/CosNotifyComm/SequencePushSupplier:1.0 """

    _FNORB_ID = "IDL:omg.org/CosNotifyComm/SequencePushSupplier:1.0"

    def disconnect_sequence_push_supplier(self, *args, **kw):
        """ Operation: IDL:omg.org/CosNotifyComm/SequencePushSupplier/disconnect_sequence_push_supplier:1.0 """

        # Typecodes for 'in' and 'inout' parameters.
        inputs = []

        # Typecodes for the result, 'inout' and 'out' parameters.
        outputs = []

        # Typecodes for user exceptions.
        exceptions = []

        # Create a request object.
        request = self._create_request("disconnect_sequence_push_supplier", inputs, outputs, exceptions)

        # Make the request!
        apply(request.invoke, args, kw)

        # Return the results.
        return request.results()

Fnorb.orb.TypeManager.TypeManager_init().add_type("IDL:omg.org/CosNotifyComm/SequencePushSupplier:1.0", "000000000000000E00000055000000000000003349444C3A6F6D672E6F72672F436F734E6F74696679436F6D6D2F53657175656E636550757368537570706C6965723A312E3000000000001553657175656E636550757368537570706C69657200", SequencePushSupplier)

#############################################################################