#Write code to prompt the user to input her/his name and age and print these details on the screen. Find the length of the name and also the age of the user after one year. The format of text should look like the sample output below.

print("Hello, user!\nWhat is your name?")
name = input("Enter your name: \n")

age = input("How old are you? \n")

print("It's nice to meet you, " + name + "!\n")

length = len(name)
print("You have " + str(length) + " letters on your name.")

year = int(age) + 1
print("You will also be " + str(year) + " in a year.") 


