### Exercise 6: Arithmetic Operation ☑️
#Develop a GUI to perform Arithmetic Operations.
#- Create a class ArithmeticOperations with the following
#- a result variable to store the result after calculation
#- a function Calculate() - To perform an arithmetic operation selected by the user.
#- You can use Combobox to provide users with options to perform selected arithmetic operations and entry widgets for the values.

import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = None

    def calculate(self, operation, value1, value2):
        if operation == "Addition":
            self.result = value1 + value2
        elif operation == "Subtraction":
            self.result = value1 - value2
        elif operation == "Multiplication":
            self.result = value1 * value2
        elif operation == "Division":
            if value2 != 0:
                self.result = value1 / value2
            else:
                self.result = "Can't divide by zero."


def calculate_result(): #calculates result
    operation = operation_combobox.get()
    value1 = float(value1_entry.get())
    value2 = float(value2_entry.get())

    calculator = ArithmeticOperations()
    calculator.calculate(operation, value1, value2)

    result_label.config(text=f"Result: {calculator.result}")


arithcalc = tk.Tk()
arithcalc.title("Arithmetic Operations")
arithcalc.geometry('300x300')
arithcalc.configure(bg='#49494a')

#labels and comboboxes
operation_label = tk.Label(arithcalc, text="Select Operation:",bg='#49494a', fg='white')
operation_label.pack()

operation_combobox = ttk.Combobox(arithcalc, values=["Addition", "Subtraction", "Multiplication", "Division"])
operation_combobox.pack()
operation_combobox.set("Addition")

#entry boxes
value1_label = tk.Label(arithcalc, text="First Number:",bg='#49494a', fg='white')
value1_label.pack()
value1_entry = tk.Entry(arithcalc)
value1_entry.pack()

value2_label = tk.Label(arithcalc, text="Second Number:",bg='#49494a', fg='white')
value2_label.pack()
value2_entry = tk.Entry(arithcalc)
value2_entry.pack()

#calculates result
calculate_button = tk.Button(arithcalc, text="Calculate",bg='orchid', command=calculate_result)
calculate_button.pack(pady=15)

#displays the result
result_label = tk.Label(arithcalc, text="Result:",bg='#49494a', fg='white', pady=10)
result_label.pack()


arithcalc.mainloop()