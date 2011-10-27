# standard recursive implementation of fib
class Fib(object):
    def fib(self, x):
        if x==0:
            return 0
        elif x==1:
            return 1

        return self.fib(x-1) + self.fib(x-2)

