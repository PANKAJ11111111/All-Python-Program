# question based on string

A = "Why fit in, When you are Born to Stand Out!"

# write the program to find out the length of the string.

print(A)
print("Length od the string : ", len(A))
print()

# write a program to check how many time alphabet 'o' incounterd in the string

print(A)
print("Number of time 'o' occure : ", A.count('o'))
print()

# write a program to convert whole string in uppercase and lowercase ?

print(A)
print("string in lower case : " ,A .lower())
print("string in upper case : ", A.upper())
print()

# write a program to convert the string into tittle ?

print(A)
print("string in tittle : ", A.title())
print()

# write a program to find index of "fit in"?

print(A)
print("Index of 'fit in' : ", A.index("fit in"))
print()


B = "OOTD.YOLO.ASAP.BRB.GTC.OTW"

#  write a program to seprate string in comma seprated value
print(B.split('.'))
print()

# write a program to seprate string in alphabatic order

b = "hello"
print(sorted(b))
print()

# write a program to remove given charater in given string
print(B)
print(B.replace(".", ""))
print()

Z = " F.R.I.E.N.D.S"

# write a program to remove (.) from the given string
print(Z)
print(Z.replace(".",""))
print()

# write a program to check how many time given substring incounter in string

X = " see is the se base concept that  why seedingse is diffecult to see"

print(X.count("se"))
print()

# take a input from user and reverse the string

s1 = input("enter string = ")
s2 = s1[-1::-1]
print(s2)
print()

# write a program to check string only contain digit

s1 = input("enter string = ")
print(s1.isdigit())
print()

# write a program to check fiven string is palindrom or not?

s1 = input("enter string = ")
s2 = s1[-1::-1]
if s1 == s2:
    print("string is palindrom")
else:
    print("string is not plaindrom")

print()

# write a program to find number of vowel in string

s1 = input("enter string = ")
n = len(s1)
count =0
for i in range(0,n):
    if s1[i] == 'a' or s1[i] == 'e' or s1[i] == 'i' or s1[i] == 'o' or s1[i] == 'u':
        count+=1

print("Total number of Vowel = ",count)
print()

# write a program to check every word in string is capital or not

s1 = input("enter string = ")
s2 = s1.title()

if s1 == s2:
    print("All word's in the string begin with capital letter")
else:
    print("All word's in the string not begin with capital letter")