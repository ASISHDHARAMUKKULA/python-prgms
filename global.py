def fun():
    global x
    global y
    y=x
    x=y
    print(x)

x=7

fun()
y=5
fun()
print(x)

