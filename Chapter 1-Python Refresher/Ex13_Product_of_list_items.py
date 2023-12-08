### Exercise 13: Product of list items☑️
#Write a program that passes a list as an argument to a function. The function should then calculate the product (values multiplied) of the list values and return this value back to the main program.

def mul_list(list):
    multiplier = 1
    for elements in list:
         ans = multiplier * elements
    return ans

test_list = [2, 2, 2]
print("Result:",mul_list(test_list))