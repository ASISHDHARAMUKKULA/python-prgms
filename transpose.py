list1=[[1,2],[3,4],[5,6]]
print(list1)
result=[[]][[]]
for i in list1:
    for j in list1:
        result[j][i]=list1[i][j]
for a in result:
    print(a)
