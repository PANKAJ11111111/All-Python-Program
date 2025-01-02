import datetime

# working with datetime date class

print("Today date ",datetime.date.today())

#create date (year, month, day)

d = datetime.date(2024,12,22)
print(d)

# get each month year and day
print("year =", d.year)
print("month = ",d.month)
print("Today date " ,d.day)


# now working with time class
t = datetime.time(12,44,22)
print(t)
#get each value h ,m ,s
print("hour = ", t.hour)
print("minute = ", t.minute)
print("second = ", t.second)


# now working with datetime class

print(datetime.datetime.now())

#create object
dt = datetime.datetime(2002,12,7,12,55,32)
print(dt)

today = datetime.datetime.now()

#access each attribute
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

#formtaing date and time using shifttime
newd = today.strftime("%A-%m-%Y %H:%M:%S")
print(newd)

print(today.strftime("%c"))
print(today.strftime("%x / %X"))
print(today.strftime("%Y"))

