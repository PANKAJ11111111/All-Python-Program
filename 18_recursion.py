# print number from n to 1 using recursion

def show(n):
    if n == 0:     # base case
        return
    print(n, end =" ")       # body of recursion
    show(n-1)      # recursive call

show(10)
print("")
show(5)