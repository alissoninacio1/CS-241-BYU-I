"""
check07a.py
You produce Civics, Odysseys, and Ferraris. You will have a base class that has the name of the car.
you should create three derived classes (Civic, Odyssey, and Ferrari) that inherit from the base class
"""

class Car:                          #base class

    """initing variables"""
    def __init__(self, name):
        self.name = "Unknown model"        
        pass

    """ get door specs method"""
    def get_door_specs(self):
        return  "Unknown doors"


#---------------------------derived classes----------------------

class Civic(Car):                   
    def __init__(self, name):
        self.name = Civic
        pass
         

class Odyssey(Car):
    def __init__(self, name):
        self.name = Odyssey
        pass


class Ferrari(Car):
    def __init__(self, name):
        self.name = Ferrari
        pass
         
#--------------------------- end of derived classes--------------    
         