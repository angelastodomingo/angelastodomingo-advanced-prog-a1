#Write a program to print Multiplication table in following format from 1 to 10 tables
#Hint: Use nested loops
# Outer loop for the base number

for n in range(1,11):
    print("Multiplication table for", n)
    
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
    print()