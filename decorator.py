from random import randint

def my_decorator(func):
    '''Return the value of func + 1'''
    def bar(*args):
        return func(*args) + 1
    return bar


@my_decorator
def foo(a, b):
    '''Return random integer in range [a, b], including both end points'''
    return randint(a,b)


print '{}'.format(foo(0,9))
