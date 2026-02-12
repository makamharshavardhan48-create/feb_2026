#Reverse List:
#Write Python code to reverse the order of elements in the given list 
#Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
print(my_list)
my_list .reverse()
print(my_list)

#Common Elements:
#Given two lists them.list1 and list2 , find and print the common elements between 

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
simple_list = []
for i in list1:
    for j in list2:
        if i == j:
            simple_list.append(i)
print(simple_list)


#Task 3:
#Unique Elements:
#Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
empty_list =[]
for i in original_list:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)

#task 4:
#Remove Duplicates:
#Remove duplicate elements from the given list 
#without duplicates while preserving the order.duplicated_list and print the list 

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
empty_list = []
for i in duplicated_list:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)



#Exercise 1 List Concatenation
#Write a Python script that concatenates two lists and prints the result .

list1 = [1,2,3,4,5,]
list2 = [6,7,8,9,10]
list1.extend(list2)
print(list1)


#Exercise 2 List Repetition
#Write a Python script that repeats a list three times and prints the result.

data_list=[1,2,3,4,"harsha"]
for i in range(0,3):
    print(data_list)
data_list=[1,3,4,5]
repeated=data_list*3
print(repeated)

#Exercise 3 List Removal
#Write a Python script that removes the elements at even indices from a list.

list = [1,2,3,4,5,6,7,8,9,10]
print(list[::2])

#Exercise 4 List Insertion
#Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list

my_list = [13,14,15]
print(f"original list:{my_list}")
new_numbers = [10,11,12]
my_list[:0] = new_numbers
print(f"list after insertion:{my_list}")

# 1 Square Numbers Create a list of squares of numbers from 1 to 10
result = [i**2 for i in range(1,11)]
print(result)

# Even Numbers Generate a list of even numbers from 1 to 20.
even_numbers = print([i for i in range(1,21) if i%2==0])

#Words Lengths Given a list of words, create a list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date"]
sample_list = []
for i in words:
    sample_list.append(len(i))
print(sample_list)