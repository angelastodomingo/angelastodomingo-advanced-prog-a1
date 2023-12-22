### Exercise 2: Maths ☑️
#Write a program that evaluates the following calculations for two int numbers obtained from the user and outputs the results to the console:

#```Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)```

#input functions for user to type in a number of their choice 
print("Enter two numbers, and this program will print out the sum, difference, product, quotient and remainder!")
first_num = input("Enter a first number: ")
second_num = input("Enter a second number: ")

#this will print out the answer to all operators. 
print("Sum: ", int(first_num) + int(second_num))
print("Difference: ", int(first_num) - int(second_num))
print("Product: ", int(first_num) * int(second_num))
print("Quotient: ", int(first_num) / int(second_num))
print("Remainder: ", int(first_num) % int(second_num))