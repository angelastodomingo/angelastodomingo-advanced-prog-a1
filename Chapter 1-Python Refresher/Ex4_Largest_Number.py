### Exercise 4: Largest Number ☑️ 
#Write a program to input three numbers and outputs the largest using the multiple if -else statements

print("This program will output the largest number.")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#this if-else condition will try to figure out which one is the biggest number the user has typed in.
if num1 >= num2 and num1 >= num3:
    print(num1, " is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(num2, " is the largest number.")
else:
    print(num3, " is the largest number.")
