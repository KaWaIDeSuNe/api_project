
#
# Author: ldq <15611213733@163.com>
# Date:   2016-5-11

import threading
import sys


class TIMEOUTException(Exception):
    pass


class KThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False
        self.exception = None

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        # force the thread to install our trace.
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        """hacked run function, which installs the trace."""
        sys.settrace(self.globaltrace)
        try:
            self.__run_backup()
        except Exception as e:
            self.exception = e
            setattr(self.exception, "error_detail", "")
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        return self.localtrace if why == "call" else None

    def localtrace(self, frame, why, arg):
        if self.killed is True:
            if why == "line":
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

def timeout(seconds):
    """
    timeout decorator, the specified timeout period,
    if the method is decorated in the specified period of time
    did not return, then throw timeout exception.
    """
    def timeout_decorator(func):
        """real decorator"""
        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        def _(*args, **kwargs):
            result = []
            # create new args for _new_func,
            # because we want to get the func return val to result list.
            new_kwargs = {
                "oldfunc": func,
                "result": result,
                "oldfunc_args": args,
                "oldfunc_kwargs": kwargs}
            thd = KThread(target=_new_func, kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            # kill the child thread.
            thd.kill()
            if alive:
                raise TIMEOUTException("time out.")
            elif thd.exception is not None:
                raise thd.exception
            return result[0]
        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _
    return timeout_decorator
