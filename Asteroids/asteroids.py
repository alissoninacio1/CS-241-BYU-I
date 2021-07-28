"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
Name: Álisson de Oliveira Inácio
​
The code was based on Br Burton (given by the instructor ) and Curtis Mellor video... some ideas was discussed with a team from my team assigns.
I also add different names to my methods and add a lot of comments with explanation about what I was coding
The code was modified by me.

"""
import arcade
import math

import random

from abc import ABC
from abc import abstractmethod

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

#****************************************MY CODE AND CLASSES****************************************************

class Point:
    
    """Initing of point object, that will be used by  used by Ship, Bullet and Asteroids """
    def __init__(self):
        self.x = 0
        self.y = 0
        
class Velocity:
    
    """Initing of velocity object, that will be used by Ship, Bullet and Asteroids """
    def __init__(self):
        self.dx = 0
        self.dy = 0
        
#_____________________________________BASE CLASS for BULETS, SHIPS AND ASTEROIDS_______________________
        
        """a base class to flying objects that will be inherited for the other classes"""

class FlyingObject(ABC):
    
    """Initing of a flying object, which utilizes Point and Velocity classes """
    def __init__(self, img):
        self.center = Point() 
        self.velocity = Velocity()
        
        self.alive = True     #boolean value to set alive
        self.img =  img   #code to render a img at a given location
        
        """another flying objects attributes essential to their func"""
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.radius = SHIP_RADIUS
        self.alpha = 255         # For transparency
        self.angle = 0 
        self.speed = 0
        self.direction = 0   
        
    """ All elements (ship, bullets, asteroids) should "wrap" around the edges of the screen.
    In other words, if an object goes off the right edge of the screen, it should appear on the left edge."""   
       
    def advance(self):
        self.wrap_screen()
        self.center.x += self.velocity.dx       # Moving it horizontally.
        self.center.y += self.velocity.dy        # Moving it vertically
        
        
    def is_alive(self):
        return self.alive
    
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)
        
    """ Wrapping around screen edges for the ship, bullets, and rocks
    (where objects that leave the right side of the screen appear on the left, etc.)"""
    def wrap_screen(self):
        if self.center.x > SCREEN_WIDTH:
            self.center.x -= SCREEN_WIDTH
            
        if self.center.x < 0:
            self.center.x += SCREEN_WIDTH 
            
        if self.center.y > SCREEN_HEIGHT:
            self.center.y -= SCREEN_HEIGHT
            
        if self.center.y < 0:
            self.center.y += SCREEN_HEIGHT 
            
            
            
    
    
#----------------------------------------------SHIP CLASS---------------------------------------
        
class Ship(FlyingObject):
    
    """initing methods pertaining to target class... """
    def __init__(self):
        super().__init__("images/playerShip1_orange.png")
        
        #ship variables related to 2D dimension
        self.angle =  1     #initial angle of the ship(position)
        self.center.x = (SCREEN_WIDTH/2)
        self.center.y = (SCREEN_HEIGHT/2)
        self.radius = SHIP_RADIUS
               
        
    """if an object goes off the right edge of the screen, it should appear on the left edge.""" 
    def left(self):
        self.angle += SHIP_TURN_AMOUNT 
    
    def right(self):
        self.angle -= SHIP_TURN_AMOUNT 
    
    def thrust(self):
        
        """add velocity to the ship to move back and forward(we don't have to rotate it)"""
        self.velocity.dx -= math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
    
    def opposite_Thrust(self):
        self.velocity.dx += math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
    
#---------------------------------------------BULLET CLASS------------------------------------
class Bullet(FlyingObject):
    def __init__(self, angle_ship, x_ship, y_ship):
        super().__init__("images/laserBlue01.png")
        
        #initing variables
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        
        #ship angle
        self.angle = angle_ship + 90 #to img render vertically
        self.center.x = x_ship
        self.center.y = y_ship
        
        #bullet velocity
        self.speed = BULLET_SPEED
        
        
    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle - 90)) * BULLET_SPEED   # -90 to move on the same direction
        self.velocity.dy += math.cos(math.radians(self.angle - 90)) * BULLET_SPEED
        
    def advance(self):
        super().advance()
        self.life -= 1
        if (self.life <= 0):
            self.alive = False
        
    
#----------------------------------------------BASE CLASS FOR ASTEROID AND ASTEROID CLASSES---------------------------------------
        
class Asteroid(FlyingObject):
    
    """initing methods pertaining to asteroid base class... """
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0
         
        
class Small(Asteroid):
    def __init__(self):
        super().__init__("images/meteorGrey_small1.png")
        self.radius = SMALL_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        
    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN
        
    """If a small asteroid is hit, it is destroyed and removed from the game."""    
    def apart_break(self, asteroids):
        self.alive = False

   
class Medium(Asteroid):
    def __init__(self):
        super().__init__("images/meteorGrey_med1.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        #set the medium rock velocity
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def advance(self):
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN
        
    """If hit, it breaks apart and becomes two small asteroids."""    
    def apart_break(self, asteroids):
        small1 = Small()
        small1.center.x = self.center.x
        small1.center.y = self.center.y
        #The small asteroid has the same velocity as the original medium one plus 1.5 pixels/frame up
        small1.velocity.dy = self.velocity.dy + 1.5
        small1.velocity.dx = self.velocity.dy + 1.5
        
        
        small2 = Small()
        small2.center.x = self.center.x
        small2.center.y = self.center.y
        #The second, 1.5 pixels/frame down and 1.5 to the left.
        small2.velocity.dy = self.velocity.dy - 1.5
        small1.velocity.dx = self.velocity.dy - 1.5
        
        asteroids.append(small1)
        asteroids.append(small2)
        #life status
        self.alive = False 
    
        
        
class Large(Asteroid):
    def __init__(self):
        super().__init__("images/meteorGrey_big1.png")
        self.radius = BIG_ROCK_RADIUS
        
        #asteroid movement
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        
        #velocity
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
    
    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN
        
        
    
    """ breack apart function - If a large asteroid gets hit,
    it breaks apart and becomes two medium asteroids and one small one."""
    
    def apart_break(self, asteroids):
        md1 = Medium()
        md1.center.x = self.center.x
        md1.center.y = self.center.y
        #The first medium asteroid has the same velocity as the original large one plus 2 pixel/frame in the up direction.
        md1.velocity.dy = self.velocity.dy + 2
        
        
        md2 = Medium()
        md2.center.x = self.center.x
        md2.center.y = self.center.y
        #The second medium asteroid has the same velocity as the original large one plus 2 pixel/frame in the down direction.
        md2.velocity.dy = self.velocity.dy + 2
        
        small1 = Small()
        small1.center.x = self.center.x
        small1.center.y = self.center.y
        #The small asteroid has the original velocity plus 5 pixels/frame to the right.
        small1.velocity.dy = self.velocity.dy + 5
        
        asteroids.append(md1)
        asteroids.append(md2)
        asteroids.append(small1)
        #life status
        self.alive = False 
    
#***************************************END OF MY CODE AND CLASSES**********************************************



class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()
        
        #populate with 5 asteroids
        self.asteroids = []
        
        for i in range(INITIAL_ROCK_COUNT):
            astBig = Large()
            self.asteroids.append(astBig)
            
        
        self.ship = Ship()
        
        self.bullets = []

        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        #asteroid
        for asteroid in self.asteroids:
            asteroid.draw()
            
        #bullet
        for bullet in self.bullets:
            bullet.draw()
            
        self.ship.draw()
        
        
        
        
    def remove_someAliveObjects(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
                
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)
                
    def collisions_checking(self):
        #the logic behind the colisions between ship, bullets and asteroids
        #using cartesian plane to set up the coordinates of a collision
        for bullet in self.bullets:
             for asteroid in self.asteroids:
                 if ((bullet.alive) and (asteroid.alive)):
                     x_distance = abs(asteroid.center.x - bullet.center.x)
                     y_distance = abs(asteroid.center.y - bullet.center.y)
                     distance_max = asteroid.radius + bullet.radius
                     if(x_distance < distance_max) and (y_distance < distance_max):
                         #bullet and asteroid collision
                         #call break apart func to render what we made
                         asteroid.apart_break(self.asteroids)
                         #bullet and asteroid dead
                         bullet.alive = False
                         asteroid.alive = False
                         
                         
        for asteroid in self.asteroids:
            if ((self.ship.alive) and (asteroid.alive)):
                     x_distance = abs(asteroid.center.x - self.ship.center.x)
                     y_distance = abs(asteroid.center.y - self.ship.center.y)
                     distance_max = asteroid.radius + self.ship.radius
                     if(x_distance < distance_max) and (y_distance < distance_max):
                         #ship and asteroid collision
                         #the ship is dead
                         self.ship.alive = False
    
            
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        #asteroid
        for asteroid in self.asteroids:
            asteroid.advance()
        
        #bullet
        for bullet in self.bullets:
            bullet.advance()
                
        self.remove_someAliveObjects()
        self.collisions_checking()
                
            
        self.ship.advance()

        # TODO: Check for collisions

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right()

        if arcade.key.UP in self.held_keys:
            self.ship.thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.opposite_Thrust()

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet(self.ship.angle, self.ship.center.x, self.ship.center.y)
                self.bullets.append(bullet)
                bullet.fire()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()