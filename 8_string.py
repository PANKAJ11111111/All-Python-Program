a = "hello world is the first line of code for coder."
print(a)
print(type(a))

#accessing element in the string

print(a[0])
print(a[3])
print(a[0:3])

# calculate length
print(len(a))

print(a.count('h'))

print(a.upper())

print(a.lower())

print(a.index('o'))

print(a.index("l", 10,30))

print(a.capitalize())

print(a.find('h'))

print(a.center(10 , "*"))

string1 = "my name is {} and i am {} year old".format("pankaj saratkar",25)
print(string1)

print("python123".isalnum())
print("python 123".isalnum())
print("!python".isalnum())

print("python".isalpha())
print("python123".isalpha())

print("Python".islower())
print("helloworld".islower())
print("HAPPY".isupper())

print("Happy".endswith("y"))


string = "Python Programming"

# Slice "Python"
print("Slice 1:", string[:6])  # Output: Python

# Reverse the string
print("Reverse:", string[::-1])  # Output: gnimmargorP nohtyP

# Extract "Programming"
print("Slice 2:", string[7:])  # Output: Programming

# Extract every alternate character
print("Alternate:", string[::2])  # Output: Pto rgamn

# Extract "Pro" from "Programming"
print("Slice 3:", string[7:10])  # Output: Pro