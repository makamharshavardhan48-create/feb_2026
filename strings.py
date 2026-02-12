#Problem:1
#sentence . Print the characters at even indices.

sentence = "Python is amazing"
sentence_1 = sentence[::2]
print(sentence_1)

#Problem:2

#s . Replace all spaces in the string with underscores (_)and print the modified string.

s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"

underscores = s.replace(" ",'_')
print(underscores)


#Problem:3

s = "12345"
#s . Check if the string contains only digits
s_numeric = s.isdigit()
print(s_numeric) #representing boolean value

#Problem:4
#s . Print the string in reverse order.
s = "Python is amazing"
# Output: "gnizama si nohty"
reverse_string = s [::-1]
print(reverse_string)

#Problem:5
#s . Capitalize the first letter of each word in the string and print the modified string.

s = "python programming is fun"
# Output: "Python Programming Is Fun
result=s.title()
print(result)