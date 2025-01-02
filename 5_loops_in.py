# for loop

for i in range(1,5):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(1,6):
    print("hello world")

for i in range(1,11):
    print("2 *",i," = ", 2*i)

# while loop

count = 1

while count <=5:
    print(count)
    count+=1

count = 1
while count <=10:
    print(i)
    count +=2

count = 1
while count <=5:
    print("hello world")
    count+=1

count = 1
while count <= 10:
    print("2 * ",i, " = ", 2*i)
    count+=1

# nested loop

for i in range(1,4):
    for j in range(1,11):
        print(j, end=" ")
    print("\n")


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print("")


#conditional statement

for i in range(1,10):
    if i%2 == 0:
        print(i,"is even number.")
    else:
        print(i,"is not a even number")

for i in range(1,101):
    if i%5 == 0:
        print(i,"is multiple of 5")

# break and continue

for i in range(1,10):
    if i==5:
        print("skip 5")
        continue
    else:
        print(i)

for i in range(1,10):
    if i==5:
        print("break")
        break
    else:
        print(i)