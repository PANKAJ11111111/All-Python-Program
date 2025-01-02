# problem 1
# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

r = int(input("enter number of row  = "))

for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# problem 2
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

r = int(input("enter number of row  = "))

for i in range(1,r+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# problem 3
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

r = int(input("enter number of row  = "))
i  = 1
while r != 0:
   j = r
   while j != 0:
       print(i, end=" ")
       j-=1
   i+=1
   r-=1
   print() 

# problem 4
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

r = int(input("enter number of row  = "))

i = 1
while i != r:
    for j in range(1,r-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    
    i+=1
    print()

# problem 5
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

r = int(input("enter number of row  = "))
for i in range(1,r+1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
    
print()

# problem 6
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36

r = int(input("enter number of row  = "))

for i in range(1,r+1):

    for j in range(1,i+1):
        print(i*j,end=" ")
        
    print()
print()



