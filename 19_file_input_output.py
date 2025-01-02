# import os module for deleting the file

import os 



# open method used for opening file

file = open("demp.txt", "r")

# read fuction used to resd data from file and return in form of string
# data = file.read()

#read only five character
fivechar = file.read(8)

#read line by line ues readline method

line = file.readline()

# print(data)
print(fivechar)
print(line)



line1 = file.readline()
print(line1)

#closing file is good habbit
file.close()

# open file in write mode with overwright
newfile = open("demp.txt", "w")

newfile.write("""hello evryone 
my name is pankaj saratkar
i am student of b.tech cse ai 
from medi caps university
cgpa 8.5
i am from indore""")

newfile.close()

# open file to write in append mode

newappend =  open("demp.txt", "a")

newappend.write("\nnow tell about you")

newappend.close()

# os.remove(filename) used for deleting file

n = open("practice.txt", "w")

n.write("Hi everyone \nwe learning file i/o \nusing java \ni like programming in java")

n.close()

# replace all java with python

n = open("practice.txt", "r")
data = n.read()
n.close()



newdata = data.replace("java", "python")


n = open("practice.txt", "w")

n.write(newdata)

n.close()


# program to check learing present in file or not

n = open("practice.txt", "r")
data = n.read()

if(data.find("learning") != -1):
    print("prsent")
else :
    print("absent")

n.close()
