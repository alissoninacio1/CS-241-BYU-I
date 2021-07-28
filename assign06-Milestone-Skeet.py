




"""Classes that I needed to make for this project ON THE WEEK 06
   Point and Velocity classes were used previously in the pong assing
"""

#-----------------------------------------PREVIOUS CLASSES------------------------------------

class Point:                                 
    
    """ Initing of point object, that will be used by  used by Rifle, Bullet, Target """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Velocity:
    
    """ Initing of velocity object, that will be used by Rifle, Bullet, Target """
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
        
        
 
 
#-------------------------------------------BASE CLASS for BULETS AND TARGETS--------------------------------------

""" a base class to flying objects that will be inherited for the other classes"""


class FlyingObject:
    
    """ Initing of a flying object, which utilizes Point and Velocity classes """
    def __init__(self):
        self.center = Point(0,0) 
        self.velocity = Velocity(0,0)


#----------------------------------------------BULLET CLASS---------------------------------------------------


class Bullet(FlyingObject):
   
     """initing methods pertaining to bullet class... """
    def __init__(self):
        super().__init__()                     #this will inherit the init of FlyingObjects to access centerand velocity
        self.radius = BULLET_RADIUS            #set to the global variable
        self.alive = True
       
       
    def advance(self):
        
    
    def draw(self):
        
    
    def Is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        
    def Fire(self, angle:float):
        
    
#----------------------------------------------TARGET CLASS---------------------------------------
        
class Target(FlyingObject):
   
     """initing methods pertaining to target class... """
       def __init__(self):
           super().__init__()
           self.radius = TARGET_RADIUS              #set to the global variable
           self.alive = True
        
        
        def advance(self):
        
    
        def draw(self):
        
    
        def Is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
            
        def hit():
            
        
        
        
        
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
