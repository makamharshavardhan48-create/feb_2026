#1.Create a Tuple: Write a program that creates a tuple containing three 
#elements: your name, your age, and your favorite color. Then print the tuple.
sample = ("harsha",22,"blue")
print(sample)

#2. Access Tuple Elements: Write a program that creates a tuple containing the 
#days of the week. Then, print the third element of the tuple.
day_of_the_week = ("monday","tuesday","wednesday","thursday","friday","saturday")
print(day_of_the_week[3])

#3. Tuple Concatenation: Write a program that creates two tuples, one 
#containing odd numbers from 1 to 5 and another containing even numbers 
#from 2 to 6. Concatenate these two tuples and print the result.
tuple_1 = (1,3,5)
tuple_2 = (2,4,6)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

#4. Tuple Unpacking: Write a program that defines a tuple containing the 
#dimensions of a rectangle (length and width). Then, unpack this tuple into 
#two variables and calculate the area of the rectangle.
dimensions = (10,40)
length,width = dimensions
area = length*width
print(f"area of rectangle is {area}")

#5.Write a Python program to generate a bill for a supermarket purchase. The 
#program should store the items and their prices in a list of tuples. It should 
#then iterate over this list to print out each item along with its price. Finally, 
#calculate and print the total cost of all the items

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print(f"items\t price")
print(f"-"*25)
total = 0.0
for i,j in items:
    print(f"{i}\t {j:.2f}")
    total+=j
print("-"*25)
print(f"total amount is {total:.2f}")


import task
task.expo(4,2)
task.add(4,2)

from task import*
expo(4,2)


import math
print(math.sqrt(16))
print(math.pi)
print(math.pow(2,3))

import random
print(random.randint(1,6))

from datetime import datetime
now = datetime.now()
print(now)

import os
print(os.getcwd())


