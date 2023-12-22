### Exercise C: Calculator Function☑️
#The program should display the following calculator menu:
#```
#1. Add
#2. Subtract
#3. Multiply
#4. Divide
#5. Modulus
#```
#The program will prompt the user to choose the operation choice (from 1 to 5). Then it asks the user to input values for the calculation. The program outputs the results of the calculation. The program should end by asking if the user would like to perform another calculation or not.

print("This is a calculator. It can add, subtract, multiply, divide and get the remainder.\nTo get started, select an operator: \n")

#defines the function for 'addition' operator to work, when the user selects it. 
def add():
    #I put a try block to prevent the program from crashing in case the user inputs a wrong value
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        ans = num1 + num2 
        print("The sum to",num1, "and",num2, "is", ans)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        add()
    
    selection = input("Would you like to keep using the calculator?")    
    
    if selection.lower() == "y" and selection.upper() == "Y":
        menu()
    elif selection.lower() == "n" and selection.upper() == "N":
        exit()
    else:
        print("Invalid input. Exiting the program.")
        
#defines the function for 'subtraction' operator to work, when the user selects it.         
def sub():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        ans = num1 - num2 
        print("The difference to",num1, "and",num2, "is", ans)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sub()
        
    selection = input("Would you like to keep using the calculator?")    
    
    if selection.lower() == "y" and selection.upper() == "Y":
        menu()
    elif selection.lower() == "n" and selection.upper() == "N":
        exit()
    else:
        print("Invalid input. Exiting the program.")
        
#defines the function for 'multiplication' operator to work, when the user selects it. 
def mul():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        ans = num1 * num2 
        print("The product to",num1, "and",num2, "is", ans)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        mul()
    
    selection = input("Would you like to keep using the calculator?")    
    
    if selection.lower() == "y" and selection.upper() == "Y":
        menu()
    elif selection.lower() == "n" and selection.upper() == "N":
        exit()
    else:
        print("Invalid input. Exiting the program.")

#defines the function for 'division' operator to work, when the user selects it. 
def div():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        ans = num1 / num2 
        print("The quotient to",num1, "and",num2, "is", ans)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        div()
        
    selection = input("Would you like to keep using the calculator?")    
    
    if selection.lower() == "y" and selection.upper() == "Y":
        menu()
    elif selection.lower() == "n" and selection.upper() == "N":
        exit()
    else:
        print("Invalid input. Exiting the program.")

#defines the function for 'remainder' operator to work, when the user selects it. 
def rem():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        ans = num1 % num2 
        print("The remainder to",num1, "and",num2, "is", ans)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        rem()
        
    selection = input("Would you like to keep using the calculator?")    
    
    if selection.lower() == "y" and selection.upper() == "Y":
        menu()
    elif selection.lower() == "n" and selection.upper() == "N":
        exit()
    else:
        print("Invalid input. Exiting the program.")
        
#the menu for the user to select any operator of their choice, and calculate whatever numbers they have.     
def menu():
    selection = input("Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\nPress 5 to get the remainder\n")

    if selection == '1':
        add()
    elif selection == '2':
        sub()
    elif selection == '3':
        mul()
    elif selection == '4':
        div()
    elif selection == '5':
        rem()
    
    else:
        print("Invalid input. Exiting the program.")
    
menu()