listn = ["Rose", "Rachel", "Monica", "Joe"]

# write a program to swap first and forth element

print(listn)
temp = listn[0]
listn[1]  = listn[3]
listn[3] = temp
print(listn)
print()

# write a program to add new value at secod position

listn.insert(2,"pankaj")
print(listn)
print()

# write program to delete value from the 3rd position

listn.pop(2)
print()

B =[13,7,12,10]

print(B)
print()

# write a program to multiply all the number in list
ans = 1
for i in B:
    ans*=i

print("Multiply of all the number : ",ans)
print()

# write a program to get largest number in the list

ans =0

for i in B:
    if ans < i:
        ans = i
print("lagest number in the list : ", ans )
print()

# write a program to get smallest number in the list

for i in B:
    if ans > i:
        ans = i
print("smallest number in the list : ", ans )
print()