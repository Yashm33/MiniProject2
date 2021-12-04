from products import *     #all the libraries and classes being imported from products
#import keyword is used to import the methods of a module.
#To access a module in Python, import statement is used.
#The import statement reads the code in a Python module and allows you to use it in another file.
#Like in this case in "watches" file, the methods of "products" file can be used. As products is imported. 

def menu(): #menu function is defined to print the options for the user
    print(" ___________________________________________________")
    print("|                      WATCHES                      |")
    print("|___________________________________________________|")
    print("|  0. Exit                                          |")
    print("|  1. To enter details of a analogue watch          |")
    print("|  2. To enter details of a digital watch           |")
    print("|  3. To check default records                      |")
    print("|___________________________________________________|")


while(True):   #the loop will be infinite until the user breaks it.
        menu()  #Calling the menu function from which user can choose
        #Taking the input of user's choice from menu
        optionSelected = int(input("Please Enter Your Choice : "))  
        #If the user chooses 0 then we will exit the program
        if(optionSelected == 0):
            print("Thank you!")
            break
        #If the user selects 1 then he can enter details of a analogue watch
        elif(optionSelected == 1):
            #taking inputs from user
            brand= str(input("Enter the brand of the watch: "))    
            model= str(input("Enter the model of the watch: "))
            price= float(input("Enter the price of this watch: "))
            strap_type= str(input("Enter the type of strap: "))
            strap_color= str(input("Enter the color of strap: "))
            manufacturing_year= int(input("Enter the manufacturing year of the watch: "))
            dial_shape= str(input("Enter the shape of the dial: "))
            hour_marker= str(input("Enter the type of hour marker: "))
            pointer_num= int(input("Enter the number of hands/pointers: "))
            
            watchAnalogue = analogue(brand,model,price,strap_type,strap_color,manufacturing_year,dial_shape,hour_marker,pointer_num)
            #watchAnalogue variable getting values as ananlogue class.
            print("Your Analogue Watch details: ",watchAnalogue.__str__())
            #watchAnalogue.__str__() -from this the final string in the methods will be printed from the user given data
            
        #If the user selects 2 then he can enter details of a digital watch
        elif(optionSelected == 2):
            #taking inputs from user
            brand= str(input("Enter the brand of the watch: "))
            model= str(input("Enter the model of the watch: "))
            price= float(input("Enter the price of this watch: "))
            strap_type= str(input("Enter the type of strap: "))
            strap_color= str(input("Enter the color of strap: "))
            manufacturing_year= int(input("Enter the manufacturing year of the watch: "))
            dial_color= str(input("Enter the color of the dial: "))
            numberOfDisplays= int(input("Enter the number of hands/pointers: "))
            
            watchDigital = analogue(brand,model,price,strap_type,strap_color,manufacturing_year,dial_color,numberOfDisplays)
            print("Your Digital Watch details: ", watchDigital.__str__())
        #If the user selects 3 then he can view the records which are already entered
        elif(optionSelected == 3):
            #records being entered wuth help of analogue and digital classes
            watchAnalogue1 = analogue("Rolex","GMT unworn 2021",226935.00,"metalic","silver",2021,"circle","baton indices",3)
            watchAnalogue2 = analogue("Cerutti","Ruscello CRA 200",1410.00,"Leather","Blue",2017,"circle","roman numeric",2)
            watchDigital1 = digital("Anself","1391",147.00,"Leather","black",2014,"silver",5)
            watchDigital2 = digital("Fossil","FTW291",7000.0,"silicon","black",2020,"black",7)
            print("Analogue Watch 1: ", watchAnalogue1.__str__())
            print("Analogue Watch 2: ", watchAnalogue2.__str__())
            print("Digital Watch 1: ", watchDigital1.__str__())
            print("Digital Watch 2: ", watchDigital2.__str__())
         #if the user enters other input then he will get an appropriate message and loop will be continued   
        else:
            print("Wrong Input! Please enter a valid option ")
            continue  #the loop will be continued if wrong input is there.
    

