# write a program to check given number is positive or not?

num = int(input("enter number = "))
if num >=0:
    print("Number is positive.")
else:
    print("Number is negative.")

# write a program to check given number is odd or even?

num = int(input("enter number = "))

print("number is even. ") if num%2 == 0 else print("number is odd.")

# creat an area calculator

print("\n")
print("********** AREA CALCULATOR ***************")

print("""press 1. for square 
press 2 for rectangle
press 3 for circle
press 4 triangle
""")
choise = int(input(""))

if choise == 1:
    val = int(input("enter length = "))
    print(val*val)
elif choise == 2:
    len = int(input("enter length = "))
    bre = int(input("enter breath = "))
    print(len*bre)
elif choise == 3:
    radius = int(input("enter radius of circle = "))
    print(3.14*radius*radius)
elif choise == 4:
    base = int(input("enter base = "))
    height = int(input("enter height = "))
    print(0.5*base*height)
else :
    print("invalid input ")

# check whether pass letter is vowel or not

val = input("enter character = ")

if val == 'a' or val == 'e' or val == 'i' or val == 'o' or val == 'u':
    print("character is vowel")
else :
    print("charater is not vowel")

# write program to check whether number of digit 
 
num = int(input("enter number = "))

if num//10 == 0:
    print("1")
elif num//100 == 0:
    print("2")
elif num//1000 == 0:
    print("3")
elif num//10000 == 0:
    print("4")
elif num//100000 == 0:
    print("5")
else:
    print("grater than 5")