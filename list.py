numbers=[1,2,3,4,5]
print(numbers)
nested=[[2,[37]],4,['hello']]
print(nested[0])
print(nested[1])
print(nested[2][0][3])
print(nested[2:3])
print(nested[0][1:2])
nested[1]=7
print(nested)
nested[0][1][0]=25
print(nested)
a=5
b=a
a=10
b=a
print(b)
print(a)
list1=[1,2,3,4,5]
list2=list1
print(list2)
list1[2]=6
print(list1)
print(list2)
print(list1[1:4])
print(list1[:])
list3=[4,5,6]
list4=[4,5,6]
list5=list4
print(list5)
print(list3==list4)
print(list5==list4)
print(list3 is list4)
print(list5 is list4)
print(list3+list5)
list4=list4+[8]
print(list4)
print(list5)
