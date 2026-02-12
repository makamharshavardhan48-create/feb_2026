#Task 1: Add Function
#Write a Python function named add that takes two arguments a and b and returns their sum.
def add(a,b):
    return a+b
obj = (4+5)
print(obj)

#Task 2: Square Function
#Write a Python function named square that takes a number x as input and
#returns its square.
def square(x):
    return x * x
print(square(6))

#Task 3: Factorial Function
#Write a Python function named factorial that takes a positive integer n as
#input and returns its factorial.
#def factorial(n):
 #   result = 1
 #   for i in range(1, n+1):
#        result = result * i
#        return result
#num = int(input("Enter a positive integer:"))
#print("factorial is :", factorial(num))

#Task 4: Maximum Function
#Write a Python function named maximum that takes a list of numbers as input and 
#returns the maximum value in the list .
def maximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
num = [2,3,56,78,90]
print("maximum value is:",maximum(num))

#Task 5: Reverse Function
#Write a Python function named reverse that takes a string s  as input and
#returns its reverse.
def reverse(s):
    return s [::-1]
text = "harsha"
print("reverse string: ",reverse(text))

#Task 6: Check Prime Function
#Write a Python function named is_prime that takes a positive integer n as input
#and returns True if n is prime, otherwise false.
def is_prime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
num = 6
print(is_prime(num))

#Task 7: Fibonacci Function
#Write a Python function named fibonacci that takes a positive integer n as
#input and returns the n th fibonacci number.
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return
num = 8
print("fibonacci number is :", fibonacci(num))

#Task 8: Palindrome Function
#Write a Python function named is_palindrome that takes a string s as input and
#returns True if s is a palindrome, otherwise False.
def is_palindrome(s):
    return s == s[::-1]
text = "shafiya"
print(is_palindrome(text))


#Task 9: Sum of Squares Function
#Write a Python function named sum of squares that takes a list of numbers as
#input and returns the sum of the squares of those numbers.
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total
num = [12,34,55,67,]
print("sum of squares is:", sum_of_squares(num))

#Task 10: Average Function
#Write a Python function named average that takes a list of numbers as input and
#returns the average value.
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
num = [11,33,44,22]
print("average is:",average(num))