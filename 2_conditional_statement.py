# if statemnt 

marks = 69

if marks >=90:
    print('you get mobile phone as price. ')

print("Thankyou")

# if-else statement

if marks >=35:
    print("you passed exam")
   
else :
    print("you failed the exam ")

# if-elif-else statement

if marks>=90:
    print("garde a+")
elif marks >=75:
    print("grade a")
elif marks >=60:
    print("grade b+")
elif marks >=45:
    print("grade b")
else:
    print("grade c")

#nested if else statement
age = 28
if age>=18:
    if age>=25 and age <=30:
        print("you are youger adult")
    else:
        print("you are young")
else:
    print("you are minor")