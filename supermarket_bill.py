#Name:Makam harshavardhan
#topic: super market project
#Date: 18-01-2026

name = input("enter your name:")

#list of markets in items
list = '''
rice       Rs10/kg
sugar      Rs8/kg
oil        Rs30/kg
salt       Rs25/kg
paneer     Rs40/kg
maggie     Rs12/kg
boost      Rs200/bottle
'''

#declaration
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

#rate for each items
items = {'rice':10,'sugar':8,'oia':30,'salt':25,'paneer':40,'maggie':12,'boost':200}
while True:
    option = input("press 1 for list or press 2 for exit:")
    if option == "2":
        print("Thank you for shopping")
        break
    elif option =="1":
        print(list)
        
        while True:
            input_1 = input("To buy press 1 or press 2 to exit")
            if input_1 =="2":
                print("Thank for shopping")
                break
            elif input_1 =="1":
                item = input("choose your items:").lower()
                while True:
                    quantity_input = input("enter quantity:")
                    quantity = int(quantity_input)
                    break
                else:
                    print("please enter a valid quaantity.")
            if item in item:
                price = quantity * items [item]
                pricelist.append((item,quantity,items[item], price))
                totalprice += price
                ilist.append(list)
                qlist.append(quantity)
                plist.append(price)
            else:
                print("selected item is not available.sorry for the inconvenience.")
        
        if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalprice = tax + totalprice
            
            print(25 * "=", "Makam Harshavardhan Supermarket" ,25 * "=")
            print(28 * "","ALLAGADDA")
            print("Name:",name, 30 * "")
            print(75*"-")
            print("sno", 10 * " ", 'items',8 * " " ,'quantity',8 *" ",'price')
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 *" ",qlist[i], 8 * " ", plist[i])
                print(75 * "-")
                print(50 * " ", 'Total amount:', 'Rs', totalprice)
                print("Tax amount:", 50 * " ", 'Rs', tax)
                print(75 * "-")
                print(50 * " ", 'Final amount:', 'Rs', finalprice)
                print(75 * "-")
                print(20 * " ", "Thank you & visit again")
                print(75 * "-")
                
                
            
                
