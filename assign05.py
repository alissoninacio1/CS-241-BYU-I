""" 05-prove assignment
one-player Pong game using arcade 
"""

import arcade  #to import all arcade methods
import random

#global constants to use in the program
SCREEN_WIDTH = 400 #pixels
SCREEN_HEIGHT = 300 #pixels
BALL_RADIUS =  10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5
class Point:
    def _init_(self):
        self.x
        self.y


class Velocity:
    def _init_(self):
        self.dx
        self.dy

class Ball:
    def _init_(self):
        self.center = Point()
        self.velocity = Velocity()

    def draw():
    def advance():
    def bounce_horizontal():
    def bounce_vertical():
    def restart(): 

        

class Paddlde:
    def _init_(self):
        self.center = Point()

    def draw():
    def move_up():
    def move_down():
        
window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()