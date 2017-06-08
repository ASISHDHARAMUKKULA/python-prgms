def mynum():
    print("spam")
    print("eggs")

mynum()


output:
spam
eggs

// you must define function before they are called

hello()
def hello():
     print("hello")
        
output:
  Traceback (most recent call last):
  File "A:/python prgms/functions.py", line 1, in <module>
    hello()
NameError: name 'hello' is not defined

Process finished with exit code 1  

// function with  arguments

def print_print(word):
    print(word+"!")

print_print("spam")
print_print("eggs")
print_print("python")

output:
    
spam!
eggs!
python!


// returning values from functions

def add_numbers(x,y):
    total=x+y
    return total
    print("hello")


print(add_numbers(4,5))

output:9
    
 // assigning Function to a variable.
    
    def multiply(x,y):
    return x*y

a=4
b=5
operation = multiply
print(operation(a,b))


output:20
    
    
// functions can be passed as arguments to other functions.


// example

def add(x,y):
    return x+y
def do_twice(func,x,y):
    return func(func(x,y),func(x,y))

a=5
b=6
print(do_twice(add,a,b))

output:22
    


    
    
    
    
            
