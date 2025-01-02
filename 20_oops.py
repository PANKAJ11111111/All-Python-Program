# creating class

class student:
   # class attribute
   school_name = "ABC" 

   #default constructor 
   def __init__(self):
        print("new student added..")
        
   # parametarized constuctor
   def __init__(self, fullname, marks):
        print("new student added..")
        #object attribute
        self.name = fullname
        self.marks = marks

   # method in class
   def hello(self):
       print("hello i am method of object")
    
   # method for get marks
   def getmarks(self):
       print("marks of ", self.name, " = ", self.marks)
   
   # method for set or update marks
   def updatemarks(self,newmarks):
       self.marks = newmarks
    


# creating object of class

s1 = student("pankaj",89)
print(s1.name)
print(s1.marks)
s1.hello()
s1.getmarks()
s1.updatemarks(45)
s1.getmarks()

#access class attribute
print(student.school_name)

s2 = student("naman",98)
print(s2.name)
print(s2.marks)
s2.hello()
s2.getmarks()

"""create a class student with attribute name and marks of 3 subject as argument in using constructor
 and genrate method for calculate average of the marks """

class student1 :

    def __init__(self,name, marks1, marks2 , marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def average(self):
        sum = self.marks3 + self.marks1 + self.marks2
        average = sum/3
        print("Avearge of ", self.name, " = ", average)


s3 = student1("pankaj", 45, 40, 44)
s3.average()

del s3
        

# private attribute and methos

class c:

    __name = "anonamus"
    def __init__(self):
        print("constructor called.....")
    
    def __hello(self):
        print("i am private method")
    
    def work(self):
        self.__hello()
    
    @staticmethod
    def s():
        print("i am static method")

p1 =c()
p1.work()
p1.s()
c.s()


# inheritance

# single level inheritance

class car:

    def __init__(self):
        print("car created....")
    
    def start():
        print("car started...")

    def stop():
        print("car stop...")


class toyotacar(car):

    def __init__(self):
        super().__init__()
        print("toyota car....")


t1 = toyotacar()
toyotacar.start()
toyotacar.stop()

# multiple inheritance

class mother:

    def __init__(self):
        print("i am mother.....")
    
    def motherlover(self):
        print("mother always love you")

class father:

    def __init__(self):
        print("i am father.....")
    
    def fatherlover(self):
        print("father always love you")  

class child(father,mother):

    def __init__(self):
        super().__init__()
        super().__init__()
        print("i am child")

c1 = child()
c1.fatherlover()
c1.motherlover()



# Parent Class
class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def details(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

# Child Class 1
class Book(Publication):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def details(self):
        return f"{super().details()} - Genre: {self.genre}"

# Child Class 2
class Journal(Publication):
    def __init__(self, title, author, year, volume):
        super().__init__(title, author, year)
        self.volume = volume

    def details(self):
        return f"{super().details()} - Volume: {self.volume}"

# Child Class 3
class Magazine(Publication):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue

    def details(self):
        return f"{super().details()} - Issue: {self.issue}"

# Objects for each child class
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
journal = Journal("Nature", "Various", 2023, 786)
magazine = Magazine("National Geographic", "Various", 2023, "March")

# Print details
print(book.details())
print(journal.details())
print(magazine.details())


# circle question

class Circle:

    def __init__(self, r):
        self.radius = r  # Instance attribute
    
    
    def area(self):
        print("Area of circle =", 3.14 * self.radius * self.radius)
    
    @property
    def parameter(self):
        print("parameter of circle = ", round(2*3.14*self.radius,2))


# Create an instance of Circle
c1 = Circle(5)
c1.area()  # Output: Area of circle = 78.5
c1.parameter


class employee:

    def __init__(self):
        self.name = input("enter your name = ")
        self.role = input("enter your role = ")
        self.deprt = input("enter your department = ")
        self.salary = int(input("enter your salary = "))
   
    def showdetail(self):
        print("Hello my name is ",self.name,"\nMy role is ",self.role)
        print("My department ",self.deprt,"and my salary ",self.salary)

class engineer(employee):
    def __init__(self):
        super().__init__()
        self.age = int(input("enter your age = "))
        self.ex = int(input("enter your experience = "))
    



# __gt__ dunder use

class order:

    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def showd(self):
        print("item name = ", self.item)
        print("item price = ",self.price)
    
    def __gt__(self,second):
        if(self.price > second.price):
            return True
        else:
            return False

o1 = order("kaju",450)
o2 = order("badam", 900)

print(o1>o2)
        

        
        

