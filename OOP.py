class Myclass:
    "This is Asish"

    a=10
    def fun():
        print("Hello Asish")

print(Myclass.a)
print (Myclass.fun())
print(Myclass.__doc__)
obj=Myclass()
print(Myclass.fun)
print(obj.a)
print(obj.fun)


class Employee:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name
    def display(self):
        print("rno:",self.rno,"name:",self.name)
emp=Employee(1,"A")
emp1=Employee(2,"B")
emp.display()
emp1.display()



class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def getData(self):
        print("{0}+{1}j".format(self.r,self.i))
c1=ComplexNumber()
c1.r=6
c1.i=5
c1.getData()
