### Exercise 8: Print Pattern ☑️ 
#Write a program to display the following pattern using nested loops.
#```
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#```

lines = 5
for i in range(1, lines + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
