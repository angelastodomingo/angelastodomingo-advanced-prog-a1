## Exercise 3: Line graph ☑️
#-  Draw a line in a diagram from position (1, 2) to position (6, 8)
#-  Draw a dotted line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)
 
import matplotlib.pyplot as plt

#Draw a line from (1, 2) to (6, 8)
plt.plot([1, 6], [2, 8], label='Line')

#Draw a dotted line from (1, 3) to (2, 8), (6, 1), and (8, 10)
plt.plot([1, 2, 6, 8], [3, 8, 1, 10], linestyle='dotted', label='Dotted Line')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line and Dotted Line')

#shows the graph
plt.show()