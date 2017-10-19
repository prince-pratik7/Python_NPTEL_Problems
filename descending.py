def descending(l):
    if (len(l)==0):
        return (True)
    for i in range(0,len(l)+1):
        a=l[i:]
        b=l[0:i-1]
        z=0
        for i in range(0,len(b)+1):
            if(a[z]<=b[-1]):
                z=z+1
                return (True)
            else:
                return (False)
