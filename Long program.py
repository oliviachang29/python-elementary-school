#Annoying Program
#Annoys the user by repeatedly printing() things.

long = input("Put in something long: ")
number = 0
for letter in long:
    print("Umm...hi?")
    number += 1

if number > 5:
    print("You put in something quite long! You did it", number, "whole times!")
else:
    print("Luckily your input wasn't very long.")

print("\a")
input("\n\nPress enter and quit.")
    
