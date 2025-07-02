# This is the main module that imports the add_numbers function from the addition module

# Uncomment the following lines to test the import from a different module

# import add_numbers
# from addition import add_numbers as add
# result = add_numbers.add_numbers(1,2)
# print(result)

# import addition as add
# result = add.add_numbers(1,2)
# print(result)


# from addition import add_numbers, subtract_numbers
# result = add_numbers(1,2)
# result2 = subtract_numbers(5, 3)
# print("The sum is :",result)
# print("The diff is:",result2)


# from addition import *
# result = add_numbers(1,2)
# result2 = subtract_numbers(5, 3)
# print("The sum is :",result)
# print("The diff is:",result2)

# Importing the math module to demonstrate a different import (https://docs.python.org/3/py-modindex.html)
# import math
# print(math.pi)
# print(math.factorial(5))


# Importing the random module to demonstrate a different import
# import random
# print("Random number is : ",random.randrange(101)) 
# # we can use randint as well
# print("Random number is : ",random.randint(1,100)) 



from addition import add_numbers

result = add_numbers(6,7)
print(result)
