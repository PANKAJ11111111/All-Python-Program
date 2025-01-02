#A set is a built-in data structure in Python that is unordered, mutable, and contains unique elements. It is commonly used for operations involving membership testing, deduplication, and mathematical set operations like union and intersection.

# creating set

fruit = {"apple", "banana", "mango", "orange"}
print(fruit)
print(type(fruit))
print()


# empty set
empty = set()
print(fruit)
print(type(fruit))
print()

for i in fruit:
    print(i)

fruit.add("jamun")

print(fruit.pop())

fruit.remove("apple")

fruit.discard("mango")

fruit.add(("kiwi","dragon" ,"fruit"))

print(fruit)

print("banana" in fruit)


