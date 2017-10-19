def interverse(n):
    num=0
    while n>0:
        num=num*10+n%10
        n=n//10
    return num        
        
        
