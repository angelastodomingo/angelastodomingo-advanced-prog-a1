### Exercise 13: Product of list items☑️
#Write a program that passes a list as an argument to a function. The function should then calculate the product (values multiplied) of the list values and return this value back to the main program.

#defines a function to calculates the product of all numbers
def product_list(list):
    multiplier = 1
    for elements in list:
         multiplier = multiplier * elements
    return multiplier

#this will print the product of all the numbers provided.
check = [1, 2, 3]
print("Result:",product_list(check))