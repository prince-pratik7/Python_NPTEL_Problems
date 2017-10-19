"""
Type 1
#memoised fibonacci
__fib_cache = {}
def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib(n-2) + fib(n-1)
        return __fib_cache[n]
"""
#Type 2

fibtable={}
def fib(n):
    if n in fibtable:
        return(fibtable[n])
    if n==0 or n==1:
        value=n
    else:
        value=fib(n-1)+fib(n-2)
    fibtable[n]=value
    return(value)
"""
Type 3

def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)
"""

