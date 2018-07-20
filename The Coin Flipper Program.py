#The Coin Flipper Program
#Acts like a coin flipping, and flips 100 times.

#Now create the sentry variables
counter = 0
heads = 0
tails = 0

#Wait for the user to tell me to flip
input("\nPress enter to flip a coin 100 times.")

#import the module random
import random

#Now for the while loop
while counter < 100:
    counter = counter + 1
    random_number = random.randrange(2)+ 1
    if random_number == 1:
        heads = heads + 1
    elif random_number == 2:
        tails = tails + 1
    else:
        print ("This is a broken program.")

print("\nYou flipped heads", heads, "times and flipped tails", tails, "times.")

input("\n\nPress the enter key to exit.")
