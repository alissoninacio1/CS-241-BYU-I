"""
CS241 Checkpoint 5A
"""



import random

class Ship:
   ### Initialize the ship object with default values
   def __init__(self):
      self.x = 0
      self.y = 0
      self.dx = 0
      self.dy = 0

   ### Draw the ship (show coordinates on the screen)
   def draw(self):
      print(f"Drawing ship at ({self.x}, {self.y})") 

   ### Advance the ship for 1 frame based on dx and dy
   def advance(self):
      self.x += self.dx
      self.y += self.dy


class Game:
    def __init__(self, dx, dy):
        self.ship = Ship()

        # Set the ship's initial velocity
        self.ship.dx = dx
        self.ship.dy = dy

    def on_draw(self):
        self.ship.draw()


    def update(self):
        self.ship.advance()



def main():
    """
    The main function sets up the game class and calls its
    methods repeatedly, just like will happen in actual games.
    """

    seed = input("Enter a random seed: ")
    random.seed(seed)

    dx = random.randint(-4, 4)
    dy = random.randint(-4, 4)

    print(f"Starting the ship with velocity ({dx}, {dy})")

    game = Game(dx, dy)

    for i in range(20):
        game.update()
        game.on_draw()

if __name__ == "__main__":
    main()
