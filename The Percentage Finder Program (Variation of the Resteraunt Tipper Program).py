#Percentage Calculator Program
#Calculates percentages
#Version of Resteraunt Tipper.
print("Welcome to the Percentage Calculator program!")
number = int(input("Percentage?\n"))
out_of = int(input("Out of? \n"))

#Calculate the percent
percent = number * out_of / 100


#Output the answer
print (number, "out of", out_of, "is", str(percent) + "%.")

#Finish the program.
input("\n\nPress the enter key to exit.")
