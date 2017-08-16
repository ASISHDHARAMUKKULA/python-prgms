def selection(l):

    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if(l[i]<minpos):
                minpos=i
    (l[start],l[minpos])=(l[minpos],l[start])
    return l[start], l[minpos]
l=[1,6,5,2]
a=selection(l)
print(a)
