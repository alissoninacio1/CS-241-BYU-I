"""
Prove assignment - assign03.py 

The logic of the walking methods(move methods):
    check if the fuel is suficient (fuel < 5), if not, I need to print a message saying that's insuficient.
    If yes, it needs to move according to the respective coordinates and change the position by 1, 
    subtracting 5 from fuel amount. Left and right should subtract and add 1, to x coordinate respectively... and 
    Down should add 1 to the y-coordinate, and up should subtract one from it. 

"""

class Robot:
       #__init__ is to initialize our variables, the constructor
    def __init__(self):
        self.x_coord = 10
        self.y_coord = 10
        self.fuel_level = 100

#---------------------move methods-----------------------
    #down
    def walk_down(self):
        if self.fuel_level < 5:
            print("Insufficient fuel to perform action")
        else:
            self.y_coord += 1
            self.fuel_level -= 5

    #up
    def walk_up(self):
        if self.fuel_level < 5:
            print("Insufficient fuel to perform action")
        else:
            self.y_coord -= 1
            self.fuel_level -= 5
    
    #rigth
    def walk_right(self):
        if self.fuel_level < 5:
            print("Insufficient fuel to perform action")
        else:
            self.x_coord += 1
            self.fuel_level -= 5

    #left
    def walk_left(self):
        if self.fuel_level < 5:
            print("Insufficient fuel to perform action")
        else:
            self.x_coord -= 1
            self.fuel_level -= 5

    #robot laser method, Check if the fuel amount is less then 15 in order to use laser
    # if not, I need to reduce the fuel amount by 15 and print the sound.
    def laser_fire(self):
        if self.fuel_level < 15:
            print("Insufficient fuel to perform action")
        else:
            print("Pew! Pew!")
            self.fuel_level -= 15
        
    #status
    def rob_status(self):
        print(f"({self.x_coord}, {self.y_coord}) - Fuel: {self.fuel_level}")

 

def main():
    #call the class
    robotic = Robot()
    selection = None #assigned to none value in order to get the selectors after pass the loop

    while selection != "quit":
        selection =  input("Enter command: ")

        if selection == "down":
            robotic.walk_down()

        elif selection == "up":
            robotic.walk_up()

        elif selection == "right":
            robotic.walk_right()

        elif selection == "left":
            robotic.walk_left()

        elif selection == "status":
            robotic.rob_status()

        elif selection == "fire":
            robotic.laser_fire()
    print("Goodbye.")

if __name__ == "__main__":
  main()