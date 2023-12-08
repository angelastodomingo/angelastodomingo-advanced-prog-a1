### Exercise 5: Continue ☑️ 
#Write a program that implements a while loop. This program should ask the user if they would like to continue and use the while loop to keep looping as long as they enter the letter Y. Once the while loop has terminated output the number of times it is executed.

loop_count = 0
while True:
    ans = input('press y to keep looping: ')
    if ans.lower() != "y" and ans.upper !="Y":
        break
    loop_count += 1

print("The Y is pressed and looped ",(loop_count), "times.")