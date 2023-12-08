### Exercise 12: Area Function☑️
#Code a program to display a menu on the screen that asks if the user wants to
#```
#1: Calculate the area of a square
#2: Calculate the area of a circle
#3: Calculate the area of a triangle 
#```
#Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.

def square():
    num1 = int(input("Enter number to calculate the area of square: "))
    area = num1**2
    print(f'Area of square: {area}')

def circle():
    num1 = int(input("Enter number to calculate the area of circle: "))
    pi = 3.14
    r = num1
    area = pi*(r*r)
    print(f'Area of circle: {area}')

def triangle():
    num1 = int(input("Enter height to calculate the area of triangle: "))
    num2 = int(input("Enter base to calculate the area of triangle: "))
    height = num1
    base = num2
    area = (height + base) / 2
    print(f'Area of triangle: {area}')

    

print('Select:\n1: Calculate the area of a square.\n2: Calculate the area of a circle.\n3: Calculate the area of a triangle')
selection = str(input("Press the number for the following to calculate: "))
if selection == '1':
    square()
elif selection == '2':
     circle()
elif selection == '3':
    triangle()
else:
    print("no. not found")