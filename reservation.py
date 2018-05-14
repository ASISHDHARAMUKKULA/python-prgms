travelling=input("yes or no")
while travelling=='yes':
    num=int(input("enter no.of people"))
    for n in range(1,num+1):
        name=input('name')
        age=int(input('age'))
        sex=input("M or F")
        print(name)
        print(age)
        print(sex)
print("over ")
