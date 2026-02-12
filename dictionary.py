#Task 1: Dictionary Update
#Write Python code to add a new key-value pair to the following dictionary:
# Output should be: {'name': 'python', 'age': 25, 'city': 'west godavari'}

my_dict = {"name": "python", "age": 25}
my_dict_1 = {"city":"west godavari"}
my_dict.update(my_dict_1)
print(my_dict)

#Task 2: Dictionary Access
#Write Python code to access and print the value associated with the key 'price' in 
#the following dictionary:
# Output should be: 1200

product_info = {"name": "Laptop", "brand": "Dell", "price": 1200}
product_info_1 = product_info["price"]
print(product_info_1)

#Task 3: Dictionary Removal
#Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
# Output should be: {'name': 'John', 'age': 30}

my_dict = {"name": "python" ,"age": 30,"city":"allagadda" }
removal = my_dict.pop("city")
print(my_dict)

#Task 4: Dictionary Keys
#Write Python code to print all the keys present in the following dictionary:
# Output should be: ['name', 'age', 'city']

my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())

#Task 5: Dictionary Values
#Write Python code to print all the values present in the following dictionary:
# Output should be: ['python', 25, 'tanuku']

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())