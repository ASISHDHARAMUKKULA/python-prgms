def binarysearch(list,v,l,r):
    if (r-l)==0:
        return False
    mid=(l+r)//2
    if(v==list[mid]):
        return True
    if v <= list[mid]:
        return (binarysearch(list,v,l,mid))
    else:
        return (binarysearch(list,v,mid+1,r))
list=[1,2,3,4,5]
print(list)
a=int(input("enter search element"))
l=0
r=4
b=binarysearch(list,a,0,4)
print(b)



