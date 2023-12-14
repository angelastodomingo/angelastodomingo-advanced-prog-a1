### Exercise 3: Is it Triangle ☑️ 
#Write a program that asks the user to enter the lengths of the three sides of a triangle.
#Use the triangle inequality to determine if we have a triangle: In mathematics, the triangle inequality states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side ([see here](https://en.wikipedia.org/wiki/Triangle_inequality))

print("Enter three sides of triangle")
side1 = int(input("Enter first side: ")) 
side2 = int(input("Enter second side: ")) 
side3 = int(input("Enter third side: ")) 

sides = side2 + side1
if side3 <= sides:
    print('it is a triangle.')
else:
    print('not a triangle')
    
if side1 == side2 == side3:
    print("The triangle type is: Equalateral")
elif side1 != side2 == side3 or side2 != side1 == side3 or side3 != side1 == side2:
    print("The triangle type is: Isosceles")
else:
    print("The triangle type is: Scalene")