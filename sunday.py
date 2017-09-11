# how to use decorators
from time import time

#def add(x, y=10):
    #return x + y

#before = time()
#print('add(10)',       add(10))
#after = time()
#print('time taken:', after - before)
#before = time()
#print('add(20,30)',    add(20, 30))
#after = time()
#print('time taken:', after - before)
#before = time()
#print('add("a", "b")', add("a", "b"))
#after = time()
#print('time taken:', after - before)

#@time is a decorator
from time import time
def timer(func):
    def f(*args, **Kargs):
        before = time()
        runvalue = func(*args, **Kargs)
        after = time()
        print('elapsed', after - before)
        return runvalue
    return f

@timer
def add(x, y=10):
    return x + y

@timer
def sub(x, y=10):
    return x - y

print('add(20,30)',    add(20, 30))
print('add("a", "b")', add("a", "b"))







