# write a program to find sum of all even number up to 50

sum = 0
for i in range(1,51):
    if i%2==0:
        sum +=i

print("sum of even number upto 50 = ", sum)

# write a program to write first 20 number square

for i in range(1,21):
    print(i*i)


# write a program to find sum of first 10 odd number

sum = 0
for i in range(1,11):
    if i%2 != 0:
        sum+=i
print("sum of first 10 odd number = ",sum)

# write a program to print number divisible by bot 8 and 12?

for i in range(1,101):
    if i%8 == 0 and i%12 == 0:
        print(i," is multiple of both 8 and 12 and also divisible by both of them.")

# write a program for super market billing system

print("\n\n")
print( "*"*10," SARATKAR SUPER MARKET BETUL BAZAR ", "*"*10)
while True:
    name = input("Name of the customer = ")
    total =0
    while True:
        product_name = input("enter product name = ")
        quentity = int(input("enter quentity = "))
        price = float(input("enter price of product "))
        total+=quentity*price
        repit = input("You have more item's in cart? (yes/no) = ")
        if repit == "no" or repit == "No":
            break
    print("-"*40)
    print("Name Of Customer = ",name)
    print("Total amoun to paid = ", total)
    print("-"*40)

    next = input("There are more customer (yes/no) = ")
    if next == "no" or next == "No":
        break


# write a program to get fibonacchi sereies upto 10

a = 0 
b = 1
count = 2
print(a,b,end =" ")
while count<=10:
    new = a+b
    a=b
    b = new
    print(new, end=" ")
    count+=1
print()

# write a program to check wether number is prime or not

number = int(input("enter number = "))
i =2
 
while i<number:
    if number%i == 0:
       print("number is not prime.")
       break
    i+=1
if i == number:
    print("number is prime")

print()

# write a program to check wether number is prime or not

num = int(input("enter number = "))

temp = num
rev = 0

while temp != 0:
    r = temp%10
    temp = temp//10
    rev = rev * 10 + r

if rev == num:
    print("Number is palindrom")
else:
    print("Number is not plaindrom")

print()


