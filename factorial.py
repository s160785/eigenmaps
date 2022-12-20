from threading import Thread
def fact(x):
    if x == 1:
       return x
    else:
       return x*fact(x-1)

class ThreadWithReturnValue(Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

x = int(input())
t1 = ThreadWithReturnValue(target=fact,args=(x,))
t1.start()
print(f"Factorial of {x} is {t1.join()}")


