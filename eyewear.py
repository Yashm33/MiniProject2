from products import * #all the libraries and classes being imported from products
import math as m
#math library is being imported as m.
#Math library now can be used by only "m", as "as" is used


class eyewear(product):  #class eyewear inheriting from "product" initialised
    def __init__(self,brand,model,price,frame_type,frame_material,gender,manufacturing_year):
        super().__init__(brand,model,price,manufacturing_year)
        self.frame_type = frame_type
        self.frame_material= frame_material
        self.gender= gender
        
    def discount(self):      #method discount to later change the price as per the need        
        self.price= m.ceil(self.price -(self.price*0.04)) #4% discount after each year from the manufacturing year
        #ceil is used for rounding the value to the upper integer

    def __str__(self): #function initialised for the string to be returned
        return super().__str__() + f' of {self.frame_type} frame of {self.frame_material}  '\
               f' manufactured in {self.manufacturing_year}'\
               f' for {self.gender}, '\
               f' that is of {self.price} AED. '\
               

class spectacles(eyewear):     #sub-class spectacles inheriting from "eyewear" initialised
    def __init__(self,brand,model,price,frame_type,frame_material,gender,lens_size,manufacturing_year):
        super().__init__(brand,model,price,frame_type,frame_material,gender,manufacturing_year)
        self.lens_size = lens_size
        
    def __str__(self): #function initialised for the string to be returned
        return super().__str__() + f' With lens size {self.lens_size}.'\
               
               

class sunglasses(eyewear):      #sub-class sunglasses inheriting from "eyewear" initialised
    def __init__(self,brand,model,price,frame_type,frame_material,gender,frame_color,lens_color,manufacturing_year):
        super().__init__(brand,model,price,frame_type,frame_material,gender,manufacturing_year)
        self.frame_color = frame_color
        self.lens_color= lens_color
        

    def __str__(self):     #function initialised for the string to be returned
        return super().__str__() + f' Frame color is {self.frame_color},  '\
               f' and lens color is {self.lens_color}.  '\
               



