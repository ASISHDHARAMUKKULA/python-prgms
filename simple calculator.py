while True:
    print("options:")
    print("enter 'add' add two numbers")
    print("enter 'sub' subtract two numbers")
    print("enter 'mul' multiply two numbers")
    print("enter 'div' divide two numbers")
    print("enter 'quit' to end prgram")
    user_input=input(":")
    if user_input=="quit":
        break
    elif user_input=="add":
        num1=float(input("enter a number"))
        num2=float(input("enter another number"))
        result=(num1+num2)
        print(result)
    elif user_input == "sub":
        num1 = float(input("enter a number"))
        num2 = float(input("enter another number"))
        result = (num1 - num2)
        print(result)
    elif user_input == "mul":
        num1 = float(input("enter a number"))
        num2 = float(input("enter another number"))
        result = (num1 * num2)
        print(result)
    elif user_input == "div":
        num1 = float(input("enter a number"))
        num2 = float(input("enter another number"))
        result=(num1/num2)
        print(result)

    else:
        print("unknown input")

options:
enter 'add' add two numbers
enter 'sub' subtract two numbers
enter 'mul' multiply two numbers
enter 'div' divide two numbers
enter 'quit' to end prgram
:add
enter a number1
enter another number2
result=3.0

options:
enter 'add' add two numbers
enter 'sub' subtract two numbers
enter 'mul' multiply two numbers
enter 'div' divide two numbers
enter 'quit' to end prgram
:quit

Process finished with exit code 0
