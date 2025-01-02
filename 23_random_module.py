# he random module in Python is used to generate random numbers, shuffle sequences, and make random selections. It provides a suite of functions for working with randomization.

import random

# to genrate random number between a,b include

print(random.randint(1,6))

#to genrate number between a to b-1

print(random.randrange(3,8))

# return float value between 0 to 1 any

print(random.random())

# uniform use to return float value between a, b

print(random.uniform(4,6))

l = ["apple", "mango", "banana", "kaju", "badam"]

# used to print random varibale from list
print(random.choice(l))

print(l)

# shuffle

random.shuffle(l)
print(l)

print(random.seed(8))