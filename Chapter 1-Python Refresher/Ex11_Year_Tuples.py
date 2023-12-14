### Exercise 11: Year Tuples☑️ 

#Create a tuple with values

#```year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)```

#- Access the value at index -3
#- Reverse the tuple and print the original tuple and reversed tuple 
#- Count number of times 2009 is in the tuple (use count() method) 
#- Get the index value of 2018(Use index method) 
#- Find length of given tuple(Use len() method)

year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

print(f'Index -3 in tuple: {year[-3]}')
print(f'Original year tuple: {year}')
print(f'Reversed year tuple: {sorted(year)}')
print(f'Print how many times 2009 was repeated: {year.count(2009)}')
print(f'Index value of 2018: {year.index(2018)}')
print(f'Length of the tuple: {len(year)}')
