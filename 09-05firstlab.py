# def make_html(tag, contents):
#     return '<{0}> {1} </{0}>'.format(tag, contents)
#
# def print_msg(msg):
#     message = msg
#
#     def printer():
#         print(message)
#
#     return printer
#
#
# world = print_msg('Hello, World!')
#
#import time

#def new_func(*args, **kwargs):
    #start = datetime.datetime.now()
    #start = time.time()
    #tl = time.gmtime()
    #result = method(*args, **kw)
    #tn = time.time()




    #return result

    #return timed

#import time

#@time.gmtime
#@time.clock()
#print ('{tm_hour}, {tm_min}, {tm_sec}')


import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())