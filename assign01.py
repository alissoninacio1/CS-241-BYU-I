import random
from random import randint

print ("Welcome to the number guessing game!")

the_seed_value = input("Enter random seed: ")
random.seed = (the_seed_value)

def runningGuess():
  
  numGuessed = randint(1, 100) 
  attempts = 0 
  guess = 0
  while numGuessed != guess:
  
    attempts += 1 
    guess = int(input("\nPlease enter a guess: "))
   
    if guess > numGuessed:
      print("\nHigher")
    elif guess < numGuessed:
      print("\nLower")
    else:
      print("Congratulations! You guesseed it!")
      print("It you took {} guesses.".format(attempts))
      
def playAgain():
  while not False:
    userCheck = input( "\nWould you like to play again (yes/no)? ")
    if userCheck == "yes":
      runningGuess()
    else:
      print("Thank you. Goodbye.")
      return False
      
runningGuess()
playAgain()
