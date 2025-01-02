def greeting():
    print("hello i am python")

def sum():
    a = int(input("enter number = "))
    b = int(input("enter number = "))
    return a+b

def product(a,b):
    return a*b

def default(name="guest"):
    print(f"hello {name}")


greeting()

print(sum())

print(product(5,5))

default("pankaj")

default()

default(name="raju")

# write a program to calculate length

def length(list):
    print(len(list))

# program for print element of the list

def print_element(list):

    for i in list:
        print(i)

# program for find factorial of n

def factorial_cal(n):
    ans =1
    for i in range(1,n+1):
        ans = ans*i
    
    print("factorial of ",n, " = ",ans)

# program to convert USD to INR

def convert_INR(amount):
    print(24.39*amount)

def evenodd():
    val = int(input("enter number = "))
    l = val%10
    print(l)
    if l%2 == 0:
        return "even"
    else:
        return "odd"

print(evenodd())


       