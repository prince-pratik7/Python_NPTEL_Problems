def selectionsort(l):
    #scan slices l[0:len(l)],l[1:len(l)],...
    for start in range(len(l)):
        #Finding Min. Value in Slice
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
        #... and moveing it to start of slice
        (l[start],l[minpos])=(l[minpos],l[start])
    return l
