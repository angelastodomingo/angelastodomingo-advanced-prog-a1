### Exercise 5: Continue ☑️ 
#Write a program that implements a while loop. This program should ask the user if they would like to continue and use the while loop to keep looping as long as they enter the letter Y. Once the while loop has terminated output the number of times it is executed.

#while loops help achieve the desired looping effect, until the user decides to quit it using any letter/word/number of their choosing.
loop_count = 0
while True:
    user_input = input('Press Y to keep looping: ')
    if user_input.lower() != "y" and user_input.upper() != "Y":
        break
    loop_count = loop_count+1

print("The loop was executed", loop_count, "times.")
