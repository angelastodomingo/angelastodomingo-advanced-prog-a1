## Exercise 5: Calculator☑️ 
#Develop a GUI to perform basic arithmetic operations like addition, subtraction, multiplication, Division, and modulo division using buttons. You can ask the user to enter the values in entry widget and select the operation to be performed.

import tkinter as tk
from tkinter import Label, Entry, Button

def calculate(operator): #to get it working
    try:
        num1 = float(num1entry.get())
        num2 = float(num2entry.get())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        elif operator == "%":
            result = num1 % num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result.config(text="Invalid input. Please enter valid numbers.")

calc = tk.Tk()
calc.title('GUI Calculator')
calc.geometry("500x320")

# create labels, text boxes, buttons
label1 = Label(calc, text='First Number')
label2 = Label(calc, text='Second Number')
label3 = Label(calc, text='Result')
num1entry = Entry(calc, bd=3)  
num2entry = Entry(calc)  
result_label = Label(calc, text='') 

# place widgets
label1.place(x=100, y=50)
num1entry.place(x=200, y=50)
label2.place(x=100, y=100)
num2entry.place(x=200, y=100)

#the buttons and the events 
b1 = Button(calc, text='   Add   ', command=lambda: calculate("+")) #i call calculate so it can perform math operations
b2 = Button(calc, text='Subtract', command=lambda: calculate("-"))  
b3 = Button(calc, text='Multiply', command=lambda: calculate("*"))  
b4 = Button(calc, text='Divide', command=lambda: calculate("/")) 
b5 = Button(calc, text='Remainder', command=lambda: calculate("%"))

b1.place(x=100, y=150)
b2.place(x=160, y=150)
b3.place(x=220, y=150)
b4.place(x=280, y=150)
b5.place(x=330, y=150)

label3.place(x=100, y=200)
result_label.place(x=200, y=200) 

calc.mainloop()
