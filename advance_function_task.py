#task ---1
def square_all(numbers):
    return list(map(lambda x: x**2,numbers))
my_numbers = [1,2,3,4,5]
result = square_all(my_numbers)
print(result)

#task ---2
def filter_positive(numbers):
    return list(filter(lambda a:a>0,numbers))
my_numbers = [-5,3,-6,4,-10,7]
result = filter_positive(my_numbers)
print(result)

#task ---3
from functools import reduce

def calculate_factorial(n):
    if n ==0:
        return 1
    return reduce(lambda a,b: a*b,range(1,n+1))
number = 5
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")

#----------or-----------#
import math
result = math.factorial(5)
print(result)

#task---4
def count_vowels(string):
    return reduce(lambda a,b:a+(b.lower() in 'aeiouAEIOU'),string, 0)
print(count_vowels("harshavardhan"))
   
