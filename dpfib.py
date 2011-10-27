
# finding fibonacci numbers using dynamic programming
class dpFib(object):
    def __init__(self):
        # these are the base cases
        # in addition, this is the dict to be used for storing
        # further results
        self.__result = {0: 0, 1: 1}

    def fib(self, x):
        if x in self.__result:
            return self.__result[x]

        r = self.fib(x-1) + self.fib(x-2)
        self.__result[x] = r
        return r

