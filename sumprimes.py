def isprime(n):
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
def sumprimes(x):
    num=0
    for i in x:
        if isprime(i):
            num+=i
    return num        
