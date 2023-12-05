#Write a program that evaluates the following calculations for two int numbers obtained from the user and outputs the results to the console:

#```Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)```

first_num = input("Enter a first number ")
second_num = input("Enter a second number ")

print("Sum: ", int(first_num) + int(second_num))
print("Difference: ", int(first_num) - int(second_num))
print("Product: ", int(first_num) * int(second_num))
print("Quotient: ", int(first_num) / int(second_num))
print("Remainder: ", int(first_num) % int(second_num))