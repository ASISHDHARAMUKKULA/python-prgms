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
    
    
    
    
            
