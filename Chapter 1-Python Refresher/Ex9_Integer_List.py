### Exercise 9: Integer List☑️ 

#Create an integer list and perform following operations
#- Create an int list with 10 values
#- Output the list using a for loop
#- Output the highest and lowest value
#- Sort the elements in ascending order
#- Sort the elements in descending order
#- Append two elements 
#- Print the list after appending

int_list = [1,2,3,4,5,6,7,8,9,10]

#using a for loop
print("Using a for loop")
for num in int_list:
    print (num)
    
#prints out the highest value and lowest value in the int_list, respectively
print("Highest value:", max(int_list))
print("Lowest value:", min(int_list))

#prints the int_list in ascending order
int_list.sort()
print("Ascending order: ", int_list)

#prints the int_list in descending order
int_list.sort(reverse=True)
print("Descending order: ", int_list)

#appends 11 and 12 to the list 
int_list.append(11)
int_list.append(12)

#prints the updated list after appending
print(int_list)
