# # import complete moule

# import calculator_module

# # return sum of two number
# print(calculator_module.sum(5,5))

# #find power
# print(calculator_module.pow(4,2))


# import perticular fuction and method

# from calculator_module import sum,sub

# # return sum
# print(sum(2,6))

# # return subtraction
# print(sub(7,10))

# import as name according to you

import calculator_module as cal

print(cal.sum(9,0))

print(cal.divi(10,6))

cal.printval(4,5)

print(cal.modulas(10,6))

print(cal.pow(4,5))

help(cal)