# A list in Python is a collection of ordered, mutable, and heterogeneous elements. It is one of the most versatile and widely used data structures in Python.

# empty list
empty_list =[]

# number list
number = [1,2,3,4,5]

# fruits
fruit = ["mango", "banana", "orange"]

#mixed
mixed_list = [1,"mango",3.6, True]

#nested
nested = [[1,2] , [3,4], [4,5]]

print(type(fruit))

print(empty_list)
print(number)
print(fruit)
print(mixed_list)
print(nested)


# accessing element in the list

fruits = ["apple", "banana", "cherry"]

print(fruit[0])
print(fruit[1])
print(fruit[-1])

#slicing in list

c = ['ironman', "hulk" , "thor", "caption america", "superman"]

print(c[1])
print(c[-1])
print(c[-3])
print(c[1:4])
print(c[1:])
print(c[:3])
print(c[::2])
print(c[-1::-1])

# iteration using loops

#first using for loop
for i in c:
    print(i)
print()

# iterat using index in for loop
for i in range(len(c)):
    print(c[i])
print()

# iteration using while loop
i = 0

while i<(len(c)):
    print(c[i])
    i+=1
print()

# short hand for loop

[print(i) for i in c]

# fuction in list

# len() used to find out the length of the list
print("lengtht of the lis : ", len(c))

# count("value") used to find number of perticular value present in list
print("number of hulk in list: " , c.count("hulk"))

# append("value") used to insert value at the end of the list
print(c)
c.append("pankaj")
print(c)

#insert(index, "value") used to insert vvalue at particular index

c.insert(2,"purab")

# remove("value") used to remove particular element of value in list
print(c)
c.remove("purab")


# pop(index) used to delet elemnt of particular in index
c.pop(3)
print(c)


# copy the element of one list in another using copy()

news = c.copy()
print(c)
print(news)

# exted() this function used to join or add elemnt in list
c.extend(fruit)
print(c)

# reverse used to reverse the list
c.reverse()

# sort() this function used to sort the list
print(c)
c.sort()
print(c)

# clear() this fuction used to clear all data in list
c.clear()
print(c)
