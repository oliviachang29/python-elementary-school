#Spiral Tower
#version 1 - nogui

import random

#Welcome
input("\nWelcome to Spiral Tower! Press enter to begin.")

#Choose Character
character = int(input("""\nWhat is your character?
\nEnter 1 to choose Flisky. Type: Water.
Enter 2 to choose Wobbly.   Type: Fire
Enter 3 to choose Whiskers. Type: Force.\n"""))

#prepare lists, variables and tuples
inventory = [ ]
defeatedboss = [ ]

#Choose character
if character == 1:
    namecharacter = "Flisky."
    input("\nYou choose: Flisky.")
    inventory = ["bukit of water","bukit of water", "bukit of water",
                 "waterbomb",
                 "tsunami",
                 "food fish",
                 "firelight",
                 "smashball"]
elif character == 2:
    namecharacter = "Wobbly."
    input("\nYou choose: Wobbly.")
    inventory = ["firelight", "firelight", "firelight",
                 "fire resistance",
                 "smokescreen",
                 "scorched earth",
                 "food tinder",
                 "bukit of water",
                 "smashball",]
elif character == 3:
    namecharacter = "Whiskers."
    input("\nYou choose: Whiskers. Press enter.")
    inventory = [ ]
else:
    input("Invalid number. Automatically assigned to Whiskers. Press enter.")
    character = 3

#Advance the tower
input("\nYou are advancing the tower! Press enter to continue")
print("\nYou find the Spiral Tower master. \nSpiralMaster: Gave you items. \nItems:", inventory)
print("\n\nThe first battle:", namecharacter, "vs. Scratchy.")
input("Press enter to begin the battle.")
print("Battle begin! You attack first.\nWhat item do you want to use? Here is a list of your inventory.")
print(inventory)





input("\n\nPress enter to exit.")
    
    
