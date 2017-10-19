def matmult(m1,m2):
    r1=len(m1)
    r2=len(m2)
    c1=len(m1[0])
    c2=len(m2[0])
    li=[]
    for i in range(r1):
        li.append([])
    for i in range(r1):
        for j in range(c2):
            sum=0
            for k in range(r2):
                sum=sum+li[i][k]*li[k][j]
            li[i].append(sum)
    return (li)
