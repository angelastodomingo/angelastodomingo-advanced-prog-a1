### Exercise B: Locations List ☑️ 
#Using the list 

#```locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']```


#Print the list and find the length of the list
locations = ['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

print("List of locations:", locations)
print("Length of the list:", len(locations))

#- Use sorted() to print your list in alphabetical order without modifying the actual list.
alphabetical_list = sorted(locations, key=str.lower) #Used key=str.lower so that amsterdam comes first in the list.
print("Alphabetical list:", alphabetical_list)

#- Show that your list is still in its original order by printing it.
print("Original order of the list:", locations)

#- Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
reverse_list = sorted(locations, key=str.lower, reverse=True)
print("Reverse alphabetical list:", reverse_list)

#- Show that your list is still in its original order by printing it again.
print("Original order of the list:", locations)

#- Use reverse() to change the order of your list.
locations.reverse()

#- Print the list to show that its order has changed.
print("Reversed list:", locations)

#- Use sort() to change your list so it’s stored in alphabetical order.
locations.sort(key=str.lower)#This is so amsterdam comes first in the list

#- Print the list to show that its order has been changed.
print("Alphabetical order:", locations)

#- Use sort() to change your list so it’s stored in reverse alphabetical order.
locations.sort(key=str.lower, reverse=True)

#- Print the list to show that its order has changed.
print("Changed reverse alphabetical order:", locations)

