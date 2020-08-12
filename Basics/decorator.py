from functools import wraps
#Log message decorator

## Seperation concerns

def logme(func):
    import logging

    logging.basicConfig(level = logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("called {} with args {} and these kwargs {}".format(func.__name__,
        args, kwargs))
        return func(*args, **kwargs)
    
    
    return inner
















# nested function

def outer():
    number = 5

    def inner():
        print(number)

    inner()

## first class citizen
def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


## closure

def close():
    x = 5


    def inner():
        print(x)

    return inner

def add_to_five(num):
    
    def inner():
        print(num + 5)
    
    return inner

# executions

#print(apply(add, 5, 5))
#print(apply(sub, 2, 2))

#closure = close()
#closure()

#fifteen = add_to_five(10)
#fifteen()