### Exercise 13: Product of list items☑️
#Write a program that passes a list as an argument to a function. The function should then calculate the product (values multiplied) of the list values and return this value back to the main program.

def product_list(list):
    multiplier = 1
    for elements in list:
         multiplier = multiplier * elements
    return multiplier

check = [1, 2, 3]
print("Result:",product_list(check))