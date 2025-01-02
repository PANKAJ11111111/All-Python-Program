# creating tuple

empty_tuple = ()

tuplet1 = (1,2,3,4)

fruit = ("apple", "banana" ,"mango","orange")

mixedt = (1,"apple", 3.5, False)

single = (56,)

print(type(fruit))

# acessing element in the tuple using index

print(fruit[0])
print(fruit[2])

#slicing in tuple

print(fruit[::2])
print(fruit[1:3])
print(fruit[-1::-1])
print(fruit[0::])

#concatanation

tuple1 = 1,2,2,3
tuple2 = 4,5,6,6
result =tuple1+tuple2
print(result)

#iteration using for loop

for i in fruit:
    print(i)

for i in range(len(fruit)):
    print(fruit[i])
     
# iteration using while lopp

i =0

while i < len(fruit):
    print(fruit[i])
    i+=1

# conversion of tuple to list

print("type of fruit before conversion : " ,type(fruit))
fruit = list(fruit)
print("type of fruit after conversion : " , type(fruit))

# conversion of tuple to list

print("type of fruit before conversion : " ,type(fruit))
fruit = tuple(fruit)
print("type of fruit after conversion : " , type(fruit))