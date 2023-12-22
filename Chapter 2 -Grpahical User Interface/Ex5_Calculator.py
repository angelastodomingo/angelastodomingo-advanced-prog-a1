## Exercise 5: Calculator☑️ 
#Develop a GUI to perform basic arithmetic operations like addition, subtraction, multiplication, Division, and modulo division using buttons. You can ask the user to enter the values in entry widget and select the operation to be performed.

import tkinter as tk
from tkinter import Label, Entry, Button

def calculate(operator): #defines a function to get the operators to work (addition, subtraction, etc)
    #added exception handling to deal with 
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

        result_label.config(text=f"Result: {result}",bg='#49494a', fg='white')

    except ValueError:
        result.config(text="Invalid input. Please enter valid numbers.")

calc = tk.Tk()
calc.title('GUI Calculator')
calc.geometry("500x320")
calc.configure(bg='#49494a')

# create labels, text boxes, buttons
label1 = Label(calc, text='First Number:', bg='#49494a', fg='white')
label2 = Label(calc, text='Second Number:', bg='#49494a', fg='white')
label3 = Label(calc, text='Result', bg='#49494a', fg='white')
num1entry = Entry(calc, bd=3)  
num2entry = Entry(calc)  
result_label = Label(calc, text='',bg='#49494a', fg='white') 

# place widgets
label1.place(x=100, y=50)
num1entry.place(x=200, y=50)
label2.place(x=100, y=100)
num2entry.place(x=200, y=100)

#the buttons and the events 
b1 = Button(calc, text='   Add   ', command=lambda: calculate("+"), bg='indigo', fg='white') #i call calculate so it can perform math operations
b2 = Button(calc, text='Subtract', command=lambda: calculate("-"), bg='darkviolet', fg='white')  
b3 = Button(calc, text='Multiply', command=lambda: calculate("*"), bg='violet')  
b4 = Button(calc, text='Divide', command=lambda: calculate("/"), bg='lightpink') 
b5 = Button(calc, text='Remainder', command=lambda: calculate("%"), bg='pink')

b1.place(x=100, y=150)
b2.place(x=160, y=150)
b3.place(x=220, y=150)
b4.place(x=280, y=150)
b5.place(x=330, y=150)

label3.place(x=100, y=200)
result_label.place(x=200, y=200) 

calc.mainloop()
