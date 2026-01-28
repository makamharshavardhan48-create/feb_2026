#1Vowel Checker:
#Write a Python program that takes a character as input and checks whether 
#it is a vowel or not.

#char = "aeiouAEIOU"
#char_1 = input("enter the characters")
#if char_1 in char:
    #print(f"it is vowel")
#else:
    #print("not a vowel")

#2 Age Group Classification
#Write a program that takes an age as input and classifies the person into 
#one of the following age groups:
#age=int(input("enter the age"))
#if age>=0 and age<=12:
    #print(f"you ara a child")
#elif age>=13 and age<17:
    #print(f"you are a teenager")
#elif age>=18 and age<64:
    #print(f"you are a adult")
#elif age>=65:
    #print(f"you ara a senior")
#else:
    #print("invalued values")


#Write a program that takes an integer as input and classifies it as positive, 
#negative, or zero. Use the 
#if-elif-else statement.
#num = int(input("enter the number:"))
#if num>0:
    #print(f"give {num}is positive")
#elif num<0:
    #print(f"give {num}is negative")
#else:
    #print(f"give {num}is zero")

 #4 Leap Year Checker:
#Create a program that checks whether a given year is a leap year or not. A 
#leap year is divisible by 4, but not by 100 unless it is divisible by 400.
#year=int(input("enter the year to check:"))
#if year%400==0:
    #print(f"given {year} is leap year")
#elif year%4==0 and year %100==0:
    #print(f"given{year} is leap year")
#else:
    #print(f"given {year}is not a leap year")
     
#5Calculator:
#Build a simple calculator program that takes two numbers and an operator 
#(+, -, *, /) as input and performs the corresponding operation.   

#num_1 = float(input("enter the first number:"))   
#num_2 = float(input("enter the second number"))   
#operator = input("enter operator(+,-,*,/)")
#if operator == "+":
    #print("result", num_1+num_2)
#elif operator == "-":
    #print("result",num_1-num_2)
# operator == "*":
    #print("result",num_1*num_2)
#elif operator =="/":
    #if num_2==0:
        #print("result",num_1/num_2)
    #else:
        #print("error: division by zero")
#else:
    #print("invalid operator")
    
#6 Short Hand If:
#Rewrite the following code using the short-hand 
#if statement:    
   
#val1=int(input("enter val")) 
#print(f"{val1} is even" if data%2==0 else print(f"{val1} id odd"))
    
 
#7Discount Calculator:
#Create a program that calculates the final price after applying a discount. 
#The program should take the original price and the discount percentage as 
#input.

#damage_price=int(input("enter the price:"))
#discount=int(input("enter the discount%:"))
#value=(damage_price*discount)/100
#damage_price-= value
#print(f"after discount the final cost is {damage_price}")
    
#8BMI Calculator:
#Write a program that calculates the Body Mass Index BMI using the 
#formula: BMI  weight (kg) / (height (m))^2. The program should take 
#weight and height as input.

weight=float(input("enter weight in kg:"))
height=float(input("enter height in M:"))
BMI=weight/(height)**2
print(f"BMW is :{BMW}")
