#It's just a small program to tell a person how old they are, because
#I convert their age into days, hours, minutes, and seconds using:
# age * 365 * 24 * 60 * 60 to figure out their ages.

#Greet the person
print ("\t\tWelcome! Do you want to know how old you are?")

#ask for their age and tell them that I will figure out their different ages
year_age = int(input("\nTell me how old you are in years...\n\nAnd then I will figure out your different ages!\n"))

#convert the age into days
days_age = year_age * 365

#convert the age into hours
hours_age = year_age * 365 * 24

#convert age into minutes
minutes_age = year_age * 365 * 24 * 60

#convert age into seconds
seconds_age = year_age * 365 * 24 * 60 * 60

#output the results
print("\nNow for your ages:")
print("\nYou are over", days_age, "days old.")
print("\nYou are over", hours_age, "hours old.")
print("\nYou are over", minutes_age, "minutes old.")
print("\nYou are over", seconds_age, "seconds old (and counting).")

#ask to exit
input("\n\nPress the enter key to exit.")
