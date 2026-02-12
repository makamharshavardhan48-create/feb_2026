#1 print statement 
#python program to print your name
print("Makam Harshavardhan")

# comments --->in python are used to explain code are not executed.
#single-line comment start with(#)
num_1=30
num_2=40
result=num_1+num_2
print(result)
#multi-line comment start with('''or""")
"""This program contains variables, vales,operatorss,and print statements
first line of the code contains num_1(variable)and it store a value(30)
second line of the code contains num_2(variable)and it store a value(40)
"""
#2 Data structures & Data types
simple_data=[22,23.4,"harsha"]
print(simple_data)
print(type(simple_data))#contains integer,float,and strings data types
simple_data.append("shafiya")
print(simple_data)
employee_id=(4,4,5,)
print(employee_id)
print(type(employee_id))
student_name={"harsha","sameer","shafiya"}
print(student_name)
print(type(student_name))

#3 string operations
input="35"
print(type(input))
input=float(input)
print(input)
print(type(input))

#4 concatenation string
name1="pythonlife"
name2="harshalife"
result=name1+name2 #concatenation usinf+operator
print(result) #printing result

#5 python variables
var_1=4
var_2="pythonlife"
print(var_1)
print(var_2)
#6 Type conversions
value=4.4
print(type(value))#checking the type of value
value=int(value)#coverting float to int
print(type(value))#checking the type of value after converstion

value2=33
print(type(value2))#cheking float to int
value2=str(value2)
print(value2)
print(type(value2))#checking the type of value2 after converstion

#7 simple input & output
num_1=input(("enter the number 1:")) #firs number for user
num_2=input(("enter the number2:"))#second number for user
num_1=int(num_1) #type converting string into interger for number1
num_2=int(num_2)#type converting string into interger for number2
#performing add of two numbers
result=num_1+num_2
print(result)