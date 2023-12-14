### Exercise 3: Reading to a List ☑️ 
#The file ```numbers.txt``` has a list of 100 integer numbers each on a newline. Create a python program that puts this data into a list, then output the values in integer format.


#finds numbers.txt in directory
with open("numbers.txt", "r") as file:
    # Read the file and split it into lines
    lines = file.readlines()

#to store integers
integer_list = []

for line in lines:
    try:

        num = int(line.strip())
        integer_list.append(num)
    except ValueError:

        print(f"Skipping non-integer line: {line.strip()}")


for num in integer_list:
    print(num)