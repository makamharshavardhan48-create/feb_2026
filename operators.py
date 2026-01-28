#arithmetic operators
#addition
num_1 = 3
num_2 = 4
result=num_1 + num_2
print(result)


#subtraction
num_1 = 3
num_2 = 4
result=num_1 - num_2
print(result)

#(*)
num_1 = 3
num_2 = 4
result=num_1 * num_2
print(result)

#(/)
num_1 = 10
num_2 = 4
result=num_1 / num_2
print(result)

#(//)
num_1 = 10
num_2 = 3
result=num_1 // num_2
print(result)

#(%)
num_1 = 7
num_2 = 2
result=num_1 % num_2
print(result)

#exponentiation (**)
num_1 = 10
num_2 = 2
result=num_1 ** num_2
print(result)



#assignment operators
#(+=)
rice =1000
rice += 10 #eq---->rice=rice+10
print(rice)
print(type(rice))

#(-=)
rice =1000
rice -= 10 #eq---->rice=rice-10
print(rice)
print(type(rice))

#(*=)
rice =100
rice *= 10 #eq---->rice=rice*10
print(rice)
print(type(rice))

#(/=)
rice =1000
rice /= 10 #eq---->rice=rice/10
print(rice)
print(type(rice))

#(%)
rice =900
rice %= 6 #eq---->rice=rice%10
print(rice)
print(type(rice))

#comparison operators
#(==)
product_cost_1= 1000
product_cost_2 = 1000
print(product_cost_1 == product_cost_2)
print(product_cost_1 != product_cost_2)
print(product_cost_1 <= product_cost_2)
print(product_cost_1 >= product_cost_2)
print(product_cost_1 > product_cost_2)
print(product_cost_1 < product_cost_2)


#logical operators
student_name="harsha"
student_id = 60
print(student_name == "harsha" and student_id == 60)
print(student_name == "harsh" or student_id == 60)

data_1 = True
print(not data_1)

data_2 = False
print(not data_2)

#identity operators
#(is)
data_1 = [1,2,3,4,(33,33.3)]
print(id(data_1))
data = [1,2,3,4,(33,33.3)]
print(id(data))
print(data_1 is data)
#(is not)
data_1 = 456
data_2 = 459
print(data_1 is not data_2)

#membership operators
names = ["harsha","shafiya","basha",(22,23.22,"babu"),{22,44.1,"sameer"}]
print("harsha" in names)
print("fruits" not in names)



