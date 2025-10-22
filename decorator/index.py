def may_decorator(func):
    def inner_func():
        print("start function")
        func()
        print("and function")
    return inner_func

@may_decorator
def fdaa():
    print("jjj")


fdaa()

# 2
from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


@timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j


long_time(5)




def decorator_timer(some_function):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        return result, time()-t1
    return wrapper









# def my_decorator(func):
#     def wrapper():
#         print("somthing is hapening befor ")
#         func()
#         print("dcrefr")
#     return wrapper()
#
# def say_whee():
#     print("whee")
#
# say_whee = my_decorator(say_whee)