#MINI PROJECT 2
#PDE1130 SOB 32, 33, 34, 35
#Yash Mittal M00850491
#Scenario : There is this super-class "products" which has 2 classes- "watches", and "eyewear".
#These 2 classes also have their 2 sub-classes each.
#"watches" -> "analogue", "digital"
#"eyewear" -> "specatles", "sunglasses"

 

class product():   #superclass/module is initialised
    def __init__(self,brand,model,price,manufacturing_year):   #function initialised for the attributes
        self.brand = brand
        self.model = model
        self.price = price
        self.manufacturing_year = manufacturing_year

    def __str__(self):          #function initialised for the string to be returned
        return f' a {self.brand} - {self.model}'      #string which will be returned
    
class watches(product):     #class watches inheriting "product" initialised
    def __init__(self,brand,model,price,strap_type,strap_color,manufacturing_year):      #function initialised for the attributes
        super().__init__(brand,model,price,manufacturing_year)          # getting attributes from the super class
        self.strap_type = strap_type
        self.strap_color= strap_color

    
    def __str__(self):           #function initialised for the string to be returned
        return super().__str__() + f' of {self.strap_color} {self.strap_type} strap '\
               f' that is of {self.price} AED, '\
               f' manufactured in {self.manufacturing_year}'
               # super.__str__() is the string in the parent class


class analogue(watches):  #sub-class analogue inheriting "watches" initialised
    def __init__(self,brand,model,price,strap_type,strap_color,manufacturing_year,dial_shape,hour_marker,pointer_num):
        super().__init__(brand,model,price,strap_type,strap_color,manufacturing_year)
        self.dial_shape= dial_shape
        self.hour_marker= hour_marker
        self.pointer_num= pointer_num

    def __str__(self):      #function initialised for the string to be returned
        return super().__str__() + f' with {self.dial_shape} dial, '\
               f' {self.pointer_num} pointers/hands, '\
               f' and hour marker are {self.hour_marker} '

class digital(watches):  #2nd sub-class digital inheriting "watches" initialised
    def __init__(self,brand,model,price,strap_type,strap_color,manufacturing_year,dial_color,numberOfDisplays):
        super().__init__(brand,model,price,strap_type,strap_color,manufacturing_year)
        self.dial_color= dial_color
        self.numberOfDisplays= numberOfDisplays

    def __str__(self):        #function initialised for the string to be returned
        return super().__str__() + f' with {self.dial_color} dial, '\
               f' having {self.numberOfDisplays} diplay options.'
        
