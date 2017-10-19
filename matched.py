def matched(s):
    li=[]
    for i in s:
        if i=="(":
            li.append(i)
        elif i==')':
            if len(li)==0:
                return False
            else:
                p=li.pop()
                if p is not '(':
                    return False
        if len(li)==0:
            return True
        else:
            return False
