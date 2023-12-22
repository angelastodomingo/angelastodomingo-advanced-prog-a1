### Exercise 8: Print Pattern ☑️ 
#Write a program to display the following pattern using nested loops.
#```
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#```

#this variable determines number of lines that will be printed out. 
lines = 5
#outer loops
for i in range(1, lines + 1):
    #inner loop
    for j in range(1, i + 1):
        #this will add spaces between the numbers
        print(j, end=' ')
        #this will add a new line to create a triangular pattern. 
    print('')
