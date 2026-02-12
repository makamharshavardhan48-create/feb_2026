#python simple input and output
#num_1 = input("enter the number1: ")
#num_2 = input("enter the number2: ")
#result = num_1 + num_2
#print(result)

#student_name="harsha"
#print(type(student_name))
#print(student_name)

#age_1= 23
#age_2= 24
#result = age_1 + age_2
#print(type(age_1+age_2))
#print(result)

#age=23.5
#print(type(age))
#print(age)


 




#int--->float
age = 34
print(age)
float_conversation = float(age)
print(float_conversation)
print(type(float_conversation))



#float--->int
student_id = 33.33
print(student_id)
conversation_int = int(student_id)
print(conversation_int)
print(type(conversation_int))

#str--->int
roll_num = "12345"
print(roll_num)
print(type(roll_num))
sample = int(roll_num)
print(sample)
print(type(sample))
print(sample-3456)


#fundamental part 2

#list

sample_data = [23,45.3,"harsha", (2,3,2,"robo"),{2,3,4,455.2,"papu"},[2,33,45.3,"hp"],1,1,1]
print(sample_data)
print(type(sample_data))
print(id(sample_data))
sample_data.append("shafiya")
print(sample_data)
print(id(sample_data))

#tuples

sample_data_2 = (22,34.2,"papa",[34,22.2,"shafiya"],(2,3,4,"basha"),1,1,1,{22,44,45.4,"ramu"})
print(type(sample_data_2))
print(sample_data_2)

#sets
 
data_sample3 = {2,3,3,33,33,"harsha","harsha",44,44,(44,44,3,3,6,6,56.4,56.4,"harsha")}
print(type(data_sample3))
print(data_sample3)

#dictionary
user_name = {"name1" : "harsha","name2" : "shafiya","name3" : "bashabro",1 : 222,2 : 333,(1,2) :[1,3,4],}
print(type(user_name))
print(user_name)


#complex data
num_1 = 2+5j
num_2 = 3+6j
print(num_1+num_2)
print(type(num_1))

#boolean

sample_data = True
print(sample_data)
print(type(sample_data))
print(bool(1))

sample_data = False
print(sample_data)
print(type(sample_data))
print(bool(0))


#list---->sets
student_data =["harsha","shafiya","harsha","shafiya",(4,4,4,44.4,44,44,44.4,"babu","babu")]
print(type(student_data))
student_data_2 = set(student_data)
print(student_data_2)
print(type(student_data_2))
print(id(student_data_2))
#sets--->tuples
voter_id = {"harsha","harsha",22,22,33,45}
print(voter_id)
print(type(voter_id))
voter_id_2 = tuple(voter_id)
print(voter_id_2)
print(type(voter_id_2))

#tuples--->list
sample_data = (22,33,33.3,"mama",)
print(sample_data)
print(type(sample_data))
sample_data_2 = list(sample_data)
print(sample_data_2)
print(type(sample_data_2))

#dict---->tuples
voter_id = {"name1" : "harsha","name2": "shafiya",1 : 22,}
print(voter_id)
print(type(voter_id))
voter_id_2 = tuple(voter_id)
print(voter_id_2)
print(type(voter_id_2))





age = 23
if age>=18:
    print(f"you are eligible to vote {age}")


#user_name = input("enter username:")
if user_name =="harsha":
    print(f"login sucess")
    print(f"welcome {user_name}")
#print(f"wornge")


number = 4
if number >=5:
    print(number*number)
print("not eligible ")
   
   
   
   
user_name = "harsha"  
password = "harsha1234"
if user_name == "harsha" and password == "harsha1234":
    print(f"login sucess")
    print(f"welcome {user_name}")
else:
    print(f"not match")
    
    
#user_name =input("enter username:")
#password = input("enter password:")
if user_name == "harsha" and password == "harsha1234":
    print(f"login sucess")
    print(f"welcome {user_name}")
else:
    print(f"not match {user_name}")
    
age = 17
if age>18:
    print(f"you are eligible to vote {age}")
else:
    print(f"you are not eligible to vote {age}")
    
    
#markes = int(input("enter the markes:"))
#if markes>=90 and markes<=100:
    #print(f"you got A grade {markes}")
#elif markes>=80:
    #print(f"you got B grade {markes}")
#elif markes>=70:
    #print(f"you got C grade {markes}")
#elif markes>=50:
    #print(f"you got d grade {markes}")
#elif markes>=35:
    #print(f"just pass {markes}")
#else:
    #print("invilded input")
    

#markes = int(input("enter the markes:"))
#if markes>100 or markes<0:
    #print(f"invilad inputs,copmplary match")
#elif markes>=80:
   # print(f"you got A grade {markes}")
#elif markes>=70:
    #print(f"you got B grade {markes}")
#elif markes>=50:
    #print(f"you got C grade {markes}")
#elif markes>=35:
    #print(f"just pass {markes}")
#else:
    #print("faile")
    
    
    
#user_name = (input("enter username:"))
#password = (input("enter password:"))
#if user_name == "harsha":
    #if password == "1234":
        #print(f"login sucess")
        #print(f"welcome {user_name}")
    #else:
        #print("invalid password")
#else:
    #print("invalid username")
    
    
    
#age = 17
#if age>=18:
    ## print(number*number)



#user_name = (input("enter username:"))
#password = int(input("enter password:"))
#if user_name == "harsha" and password == 1234:
    #print(f"login sucess")
    #print(f"welcome {user_name}")
#else:
    #print("invilad data")
    
    
    
#product_price = int(input("enter prouductprice:"))
#if product_price>200 or product_price<0:
    #print(f"compalary match >200 or <0")
#elif product_price>=190:
    #print(f"this is RICE 190 ")
#elif product_price>=150:
    #print(f"this is OIL grather than 150 ")
#elif product_price>=35:
    #print(f"this is a MATCHBOX under 35")
#else:
    #print("invalide productprice")
    
    
    
#user_name = (input("enter username:"))
#password = int(input("enter password:"))
#otp = int(input("enter otp:"))
#if password == 12345:
        #if otp == 456:
            #print(f"login sucess")
            #print(f"welcome {user_name}")
            #print(f"thank for you otp giving {otp}")
        #else:
            #print("invalide password")
            #print("invalide otp")
#else:
    #print("invalide username")
    #print("invalide otp")
    
    
    
    
    
#user_name = {"harsha","shafiya","basha","subbu"}
#for i in user_name:
    #print(f"welcome to hp laptops {i}")
    
    
#fruits = ["banana","apple","graphs"]
#for i in fruits:
    #if i =="banana":
        #print(f" {i}")
        
        
#for i in range(1,21):
    #for j in range(1,11):
        #print(f"{i}x{j}={i*j}")
    #print("-"*25)
        
        

#for i in range(1,11):
    #if i%2==0:
        #print(i)
        
#count = 0
#while count<=2:
    #print(count)
    #count+=1




#outer =0
#while count<3:
    #SSinner =0
    #while count<2:
        #print(outer+inner)
    #outer+=1
    
def vote():
    age = 20
    if age>=18:
        print("eligible to vote")
vote()

def add(a,b):
    print(a+b)
add(10,5)

def mul(num_1,num_2):
    return num_1*num_1
obj = mul(10,10)
print(obj)
    
def arg(**a):
    return a
obj = arg(a=1,b=2,c=3)
print(obj)


def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def expo(a,b):
    print(a**b)
def mul(a,b):
    print(a*b)

