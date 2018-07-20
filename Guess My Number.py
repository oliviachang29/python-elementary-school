# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
#There is a limted number of guesses: 10 per game

import random  

print("Welcome to Guess My Number!")
print("\nI'm thinking of a number between 1 and 100.")
print("\nYou have ten tries.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
tries_two = 1

# guessing loop
while guess != the_number and tries < 10:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Try Again: "))
    tries_two += 1
    tries += 1    
        
            
if guess == the_number:
    print("\nYou guessed it!  The number was", the_number)
    print("And it only took you", tries_two, "tries!\n")
else:
    print("Sorry, you ran out of tries. Game Over.")
    print("The number was", the_number,".")
  
input("\n\nPress the enter key to exit.")
