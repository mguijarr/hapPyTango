import gevent
from gevent import monkey; monkey.patch_all(thread=False)
from IPython.core.interactiveshell import InteractiveShell
from IPython.lib.inputhook import allow_CTRL_C, ignore_CTRL_C, stdin_ready
from IPython.lib.inputhook import InputHookManager

def create_inputhook_gevent(mgr):
    """Create an input hook for running the gevent event loop.

    Parameters
    ----------
    mgr : an InputHookManager

    Returns
    -------
    An inputhook 
    """

    # Re-use previously created inputhook if any
    ip = InteractiveShell.instance()
    if hasattr(ip, '_inputhook_gevent'):
        return ip._inputhook_gevent

    got_kbdint = [False]

    def inputhook_gevent():
        """PyOS_InputHook python hook for Gevent.
        """
        try:
            ignore_CTRL_C()
            gevent.sleep(0.01)
            while not stdin_ready():
                gevent.sleep(0.05)
        except:
            ignore_CTRL_C()
            from traceback import print_exc
            print_exc()
        finally:
            allow_CTRL_C()
        return 0

    def preprompthook_gevent(ishell):
        if got_kbdint[0]:
            mgr.set_inputhook(inputhook_gevent)
        got_kbdint[0] = False

    ip._inputhook_gevent = inputhook_gevent
    ip.set_hook('pre_prompt_hook', preprompthook_gevent)

    return inputhook_gevent

def enable_gevent_hook():
    mgr = InputHookManager()
    mgr.set_inputhook(create_inputhook_gevent(mgr))

