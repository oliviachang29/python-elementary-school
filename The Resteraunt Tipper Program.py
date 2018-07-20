#The Resteraunt Tipper Program
#It prompts the user for the bill total, and then asks for a percentage for the
#bill total.
#Credits to Olivia and Lerkling Chang.
#I intend to add a user's input on how good the resteraunt was, and then tell
#the user how much percentage they should pay. Give credit to Da Yi when I do.

#prompt for the bill and the percentage to pay
print("Welcome to the Resteraunt Bill Total Program!")
bill = int(input("How much did you spend in a resteraunt today?\nSince you are rich, avoid cents and use dollar amounts:\n$"))
percent = int(input("What percent out of that money do you intend to tip the waiter?\n"))

#Calculate the tip
tip = percent * bill / 100
total = tip + bill

#Output the answer
print (tip, "is how much you tip the waiter.")
print (total, "is how much money you pay in total.")

#Finish the program.
input("\n\nPress the enter key to exit.")
