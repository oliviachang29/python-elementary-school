#The Fortune Cookie Simulator Program
#Simulates a Fortune Cookie.

#import the module random
import random

#Generate the random fortune number.
fortune_number = random.randint(1,5)

#Welcome the user
print("\t\tWelcome...I will tell you your fortune...\n")
x = input("Now... put your hands on the keyboard...\nand press enter.\n")
print("I feel...")

if fortune_number == 1:
    print("Your lucky days arrives.")
elif fortune_number == 2:
    print("The worst has ended; the rainbow is yet to come.")
elif fortune_number == 3:
    print("It's your lucky day!")
elif fortune_number == 4:
    print("Gloom, death, sorrow, despair... isn't going to happen.")
elif fortune_number == 5:
    print("Yo.")

input("\n\nPress the enter key to exit.")
