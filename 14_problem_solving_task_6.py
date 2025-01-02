# Create a dictionary to store the details of a student: Name, Roll Number, Class, and Marks in three subjects.

student = {}

i = 1

while i<=3:
    n =  input("enter name of student {} = ".format(i))
    a =  input("enter age of studenr {} = ".format(i))

    miniinfo = {}
    miniinfo.update({"name":n})
    miniinfo.update({"age":a})
    student.update({"s{}".format(i) : miniinfo})
    i+=1

print(student)

# ccessing Values
# Given the dictionary below, access and print the values of the following:

# Employee name
# Employee department
# Employee salary

employee = {"name": "Alice", "department": "IT", "salary": 50000}

print(employee["name"])
print(employee["department"])
print(employee["salary"])


# Add Key-Value Pairs
# Add a new key-value pair (age: 25) to the following dictionary:

person = {"name": "John", "city": "New York"}

person.update({"age":25})
print(person)


# Iterate Over Dictionary
# Write a program to iterate over the following dictionary and print all the keys and values:


fruits = {"apple": 10, "banana": 20, "cherry": 15}

for x ,y in fruits.items():
    print(x,":",y)


# Merge Two Dictionaries
# Merge the following two dictionaries into one:


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)


# Remove a Key
# Remove the key 'age' from the following dictionary:


person = {"name": "John", "age": 25, "city": "New York"}

person.pop("age")
print(person)

# Reverse a Dictionary
# Reverse the keys and values of the following dictionary:

original = {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}

# Reverse keys and values
reversed_dict = {value: key for key, value in original.items()}

print(reversed_dict)

# given the following nested dictionary, write code to:

# Print John's age
# Update Alice's grade to "A+"

students = {
    "John": {"age": 20, "grade": "B"},
    "Alice": {"age": 22, "grade": "A"},
}

print(students["John"]["age"])
print(students["Alice"]["grade"])
