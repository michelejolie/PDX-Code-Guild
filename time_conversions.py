import time

def time_func(func, *args):
    def wrapper(x, y):
        start = time.time()
        func(x, y)
        end = time.time()
        print(end - start)


    return wrapper

@time_func
def add_2(x, Y):
    return x + Y

add_2(5, 5)
