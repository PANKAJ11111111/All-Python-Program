import pickle

# Data to save
user1 = {
    "name": "pankaj",
    "password": "Pankaj@96",
    "age": 20
}

user2 = {
    "name": "raju",
    "password": "Pankaj@95",
    "age": 23
}

marks = [55, 66, 3, 2, 66]

# Save data to file
file = open("demp.txt", "wb")
pickle.dump(user1, file)
pickle.dump(user2, file)
pickle.dump(marks, file)
print("Data saved in file.")
file.close()

# Read data from file (Partial Read)
readfile = open("demp.txt", "rb")

print("\nReading limited data from file:")
try:
    # Limit the number of reads (e.g., 2 items only)
    for _ in range(5):
        data = pickle.load(readfile)
        print(data)
except EOFError:
    print("\nReached the end of the file.")
finally:
    readfile.close()


# get direct byte code

print("code data of user 1..")
code = pickle.dumps(user1)

# convert byte code to original data

ans = pickle.loads(code)
print("\n converted data in original form")
print(ans)

