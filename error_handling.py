#Type of errors

#value error:
#try:
 #   int("harsha")
#except ValueError as e:
 #   print(e)
    
#zero devision error:
#num_1 = int(input("enter the number1:"))
#num_2 = int(input("enter the number2:"))
#try:
##except ZeroDivisionError as e:
 #   print(e)
 
 
#file not found error:
#try:
##   file.close()
#except FileNotFoundError as e:
#    print(e)
 
 
#index error:
#list_1 = [1,2,3,4,5]
#try:
 #   if list_1[5] ==6:
 ##       print("6 exist")
 #   else:
#print("not ")
#except IndexError as e:
#    print(e)

#key error:
dict_names = {"harsha":1,"shafiya":2,"basha":3}
try:    
    dict_names_2 = dict_names["prabhas"]
    print(dict_names_2)
except KeyError as e:
    print(e)
    
#attribute error :
#class sample():
 #   def sample1(self,):
  #      print("sample1 block")
   # def sample2(self,):
 #       print("sample2 block")
#obj=sample()
#try:
 #   obj.sample3
#except AssertionError as e:
 #   print(e)


#over flow error :


#import math

#try:
#    result = math.exp(1000)  
#    print(result)
##   print("OverflowError occurred:", e)

#zerodeivisionerror:
try:
    num = 10
    result = num / 0  
    print("Result:", result)
except ZeroDivisionError as e:
    print("Runtime Error occurred:", e)