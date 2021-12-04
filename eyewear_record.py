from eyewear import *    #all the libraries and classes being imported from eyewear


#records being entered 
spectacle1 = spectacles("Spectus","Neveda",399,"rimless","stainless steel","men","55 mm",2013)
spectacle2 = spectacles("The Book Club","The Art of the Eel",259,"full rim","metal","women","47 mm",2019)
#printing with original price
print('Spectacle 1: ' + spectacle1.__str__())
print("\n")
#since manufacturing date till current year, user is getting discount.
#this is done by using the discount method, which was initialised in the eyewear class
for i in range(2013,2021):
    spectacle1.discount()  #discount() method used
    print(i)  #years displayed 
print("\n")
#printing after the discount
print('Spectacle 1 after discount: ' + spectacle1.__str__())
print("\n")
#entering another record and printing the discount in the same way as spectacle1
print('Spectacle 2: ' + spectacle2.__str__())
print("\n")
for i in range(2019,2021):
    spectacle2.discount() #discount() method used
    print(i)
print("\n")
print('Spectacle 2 after discount: ' + spectacle2.__str__())


#Now, 2 records for sunglasses class being entered and printed, along with their discounted record
sunglass1 = sunglasses("30Sundays","Daredevil",369,"full rim","acetate","men","black","gray","2021")
sunglass2 = sunglasses("BlackOut","Midnight",199,"full rim","metal","women","gray","gray",2018)

print('Sunglass 1: ' + sunglass1.__str__())
print("\n")
for i in range(2021,2021):
    sunglass1.discount()  #discount() method used
    print(i)
print("\n")
print('Sunglass 1 after discount: ' + sunglass1.__str__())
print("\n")

print('Sunglass 2: ' + sunglass2.__str__())
print("\n")
for i in range(2018,2021):
    sunglass2.discount()  #discount() method used
    print(i)
print("\n")
print('Sunglass 2 after discount: ' + sunglass2.__str__())
print("\n")


