import timeit

print "Benchmarking recursion versus dynamic programming:"
print ""
print ""
print "Recursive fib(5):"
print timeit.Timer('f.fib(5)', 'from fib import Fib; f=Fib(); gc.enable()').timeit(1)
print ""
print "DP fib(5)"
print timeit.Timer('f.fib(5)', 'from dpfib import dpFib; f=dpFib(); gc.enable()').timeit(1)
print ""
print ""
print ""
print "Recursive fib(15):"
print timeit.Timer('f.fib(15)', 'from fib import Fib; f=Fib(); gc.enable()').timeit(1)
print ""
print "DP fib(15)"
print timeit.Timer('f.fib(15)', 'from dpfib import dpFib; f=dpFib(); gc.enable()').timeit(1)
print ""
print ""
print ""
print "Recursive fib(30):"
print timeit.Timer('f.fib(30)', 'from fib import Fib; f=Fib(); gc.enable()').timeit(1)
print ""
print "DP fib(30)"
print timeit.Timer('f.fib(30)', 'from dpfib import dpFib; f=dpFib(); gc.enable()').timeit(1)
print ""
print ""
print ""
print "Recursive fib(35):"
print timeit.Timer('f.fib(35)', 'from fib import Fib; f=Fib(); gc.enable()').timeit(1)
print ""
print "DP fib(35)"
print timeit.Timer('f.fib(35)', 'from dpfib import dpFib; f=dpFib(); gc.enable()').timeit(1)
