# creating dictonary 

person = {"name":"pankaj", "age":25, "gender":"male"}

#using dict() function 

student = dict(name="prashant", age=12, section="6th", roll=34 )

print(person)
print(student)

# accessing elemen
print(student["age"])
print(person["name"])

print(student.get("name","not specified"))
print(person.get("occupation", "not specified"))

# iterating over element 

# accessing key
for i in student:
    print(i)

# accesssing value

for i in person:
    print(person[i])

#using value fuction

for i in person.values():
    print(i)

#using item fuction

for x, y in student.items():
    print(x,":",y)

dict = {
    "name":"pankaj saratkar",
    "age":34,
    "marks" :[1,2,3,4],
    "like" :("mango","orange"),
    "is_Adlut":True
}

print(dict)
print(type(dict))

dict["name"] = "sharda"
dict["surname"] = "saratkar"
print(dict)


#nested dictionary

student = {
    "name":"pankaj saratkar",
    "marks":{
        "phy":56,
        "chem":88,
        "myth":90,
    },
    "address":{
        "house_no":101,
        "colony":"shri nath colony ",
        "state":"madhya prades"
    }
}

print(student)
print(student["marks"])
print(student["marks"]["phy"])