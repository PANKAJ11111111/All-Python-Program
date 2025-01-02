x =25

def myf():
    print("inside fuction :",x)

print("Outside fuction :" ,x)
myf()


def myf2():
    x = 24
    print("inside fuction :", x)

print("outside fuction :", x)
myf2()


def myf3():
    global x
    x = 100
    print("inside fuction :", x)

print("outside fuction :", x)
myf3()
print("outside fuction :", x)


def outer_function():
    x = 5

    def inner_function():
        nonlocal x
        x += 1
        print("Inner x:", x)

    inner_function()
    print("Outer x:", x)

outer_function()


def evenodd():
    val = int(input("enter number = "))
    l = val%10
    print(l)
    if l%2 == 0:
        return "even"
    else:
        return "odd"

print(evenodd())
