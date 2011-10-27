# standard recursive implementation of fib
class Fib(object):
    def fib(self, x):
        if x==0:
            return 0
        elif x==1:
            return 1

        return self.fib(x-1) + self.fib(x-2)

# finding fibonacci numbers using dynamic programming
class dpFib(object):
    def __init__(self):
        # these are the base cases
        # in addition, this is the dict to be used for storing
        # further results
        self.result = {0: 0, 1: 1}

    def dpfib(self, x):
        if x in self.result:
            return self.result[x]

        r = self.dpfib(x-1) + self.dpfib(x-2)
        self.result[x] = r
        return r

