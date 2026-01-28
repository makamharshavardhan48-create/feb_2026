#Task 1: Set Intersection
#Write Python code to find and print the intersection of the following two sets:
# Output should be: {4, 5}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)

#Task 2: Set Union
#Write Python code to find and print the union of the following two sets:
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)

#Task 3: Set Difference
#Write Python code to find and print the elements present in set1 but not in set2:
#output should be:{1,2,3}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.difference(set2)
print(set3)

#Task 4: Set Symmetric Difference
#Write Python code to find and print the symmetric difference of the following two sets:
# Output should be: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.symmetric_difference(set2)
print(set3)

#Task 5: Set Membership Test
#Write Python code to check if the element 3 is present in the set my_set:
# Output should be: True
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

#Exercise 1: Set Intersection
#Write a Python script that finds and prints the intersection of two sets.
set_intersection = {1,3,4,5,6,"harsha","shafiya",}
set_intersection2 = {1,3,4,"harsha","babu"}
set_intersection3 = set_intersection.intersection(set_intersection2)
print(set_intersection3)

#Exercise 2: Set Union
#Write a Python script that finds and prints the union of two sets.
set_1 = {1,2,3,4,5,"harsha"}
set_2 = {1,3,4,6,7,8,9,"harsha","shafiya",}
set_3 = set_1.union(set_2)
print(set_3)

#Exercise 3: Set Difference
#Write a Python script that finds and prints the difference between two sets.
set_1 = {1,2,3,4,5,"harsha"}
set_2 = {1,3,4,6,7,8,9,"harsha","shafiya",}
set_3 = set_1.difference(set_2)
print(set_3)

#Exercise 4: Set Symmetric Difference
#Write a Python script that finds and prints the symmetric difference between two sets.
set_1 = {1,2,3,4,5,"harsha"}
set_2 = {1,3,4,6,7,8,9,"harsha","shafiya",}
set_3 = set_1.symmetric_difference(set_2)
print(set_3)