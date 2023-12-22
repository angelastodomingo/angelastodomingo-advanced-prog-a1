### Exercise 12: Area Function☑️
#Code a program to display a menu on the screen that asks if the user wants to
#```
#1: Calculate the area of a square
#2: Calculate the area of a circle
#3: Calculate the area of a triangle 
#```
#Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.

print("This program will calculate the area of a square, circle or triangle.")

#defines the function to calculate the area of a square.
def square():
    #I put a try block to prevent the program from crashing in case the user inputs a wrong value
    try:
        num1 = int(input("Enter number to calculate the area of square: "))
        area = num1**2
        print(f'Area of square: {area}')
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        square()

#defines the function to calculate the area of a circle.
def circle():
    try:
        num1 = int(input("Enter number to calculate the area of circle: "))
        pi = 3.14
        r = num1
        area = pi*(r*r)
        print(f'Area of circle: {area}')
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        circle()

#defines the function to calculate the area of a triangle.
def triangle():
    try:
        num1 = int(input("Enter height to calculate the area of triangle: "))
        num2 = int(input("Enter base to calculate the area of triangle: "))
        base = num1
        height = num2
        area = (base * height) / 2
        print(f'Area of triangle: {area}')
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        triangle()

#defines the function for user to select a shape of their choice 
def menu():
    print('Select a shape:\n1: Square\n2: Circle\n3: Triangle')
    selection = str(input("Press the number for the following to calculate: "))
    if selection == '1':
        square()
    elif selection == '2':
        circle()
    elif selection == '3':
        triangle()
    else:
        print("Invalid input.")
#this is put at the end so that this is the first thing the user sees, reads, and be able to make a choice. 
menu()