## Exercise 3: Calculator☑️
#Write a program that will display the following calculator menu 
#```
#1. Add
#2. Subtract
#3. Multiply
#4. Divide
#5. Modulus
#6. Check greater number
#```
#The program will prompt the user to choose the operation choice (from 1 to 6). Then it asks the user to input values for the calculation. The program outputs the results of the calculation.Use operator module functions

import operator

def calculator():
    print("The calculator menu.\n\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Check greater number\n\nPress Q to quit.")


    while True:
        try:
            choice = input("Select an option (1-6):\n")
            if choice == "Q" or choice == "q":
                print("Closing calculator. Goodbye!")
                break

            choice = int(choice)
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == 1:
                result = operator.add(num1, num2)
            elif choice == 2:
                result = operator.sub(num1, num2)
            elif choice == 3:
                result = operator.mul(num1, num2)
            elif choice == 4:
                result = operator.truediv(num1, num2)
            elif choice == 5:
                result = operator.mod(num1, num2)
            elif choice == 6:
                result = num1 if num1 > num2 else num2

            print("Result:", result)
        except ValueError:
            print("Invalid input. Please try again.")

calculator()