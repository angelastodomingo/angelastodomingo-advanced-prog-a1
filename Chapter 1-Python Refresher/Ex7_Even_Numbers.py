### Exercise 7: Even Numbers ☑️ 
#Write a program that prints the even numbers from 1 to 100. 
#Hint - Use Continue Statement

#used for loops to print numbers 1=100 again, but used the continue function this time. 
for i in range (1,101):
    if i%2 == 1:
        continue
    print(f'{i} - Even')