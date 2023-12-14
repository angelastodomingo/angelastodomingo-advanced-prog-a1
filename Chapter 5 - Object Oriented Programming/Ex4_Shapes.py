### Exercise 4: Shapes ☑️
#Develop a GUI using Tkinter to calculate the area of Shapes.
#Create a parent class called Shape. This should have the following methods
#```inputSides()``` – Ask the user to enter the sides of the shape. Now create subclasses for a circle, rectangle, and triangle. These should include an appropriate ``` area()``` method that will use the side values from the shape class.

import tkinter as tk
import math

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass 

class Circle(Shape):
    def inputSides(self):
        radius = float(radius_entry.get())
        self.sides = [radius]

    def area(self):
        return math.pi * self.sides[0] ** 2

class Rectangle(Shape):
    def inputSides(self):
        length = float(length_entry.get())
        width = float(width_entry.get())
        self.sides = [length, width]

    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def inputSides(self):
        base = float(base_entry.get())
        height = float(height_entry.get())
        self.sides = [base, height]

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]

def calculate_area():
    shape_type = shape_choice.get()
    shape = None

    if shape_type == "Circle":
        shape = Circle()
    elif shape_type == "Rectangle":
        shape = Rectangle()
    elif shape_type == "Triangle":
        shape = Triangle()

    if shape is not None:
        shape.inputSides()
        area_result.config(text=f"Area: {shape.area()}")
    else:
        area_result.config(text="Invalid shape selected.")

shapeareawin = tk.Tk()
shapeareawin.title("Shapes")
shapeareawin.geometry('300x300')
shapeareawin.configure(bg='#49494a')

#dropdown menu for user to select shapes 
shape_label = tk.Label(shapeareawin, text="Select a shape:", bg='#49494a', fg='white')
shape_label.pack()

shape_choice = tk.StringVar()
shape_dropdown = tk.OptionMenu(shapeareawin, shape_choice, "Circle", "Rectangle", "Triangle")
shape_dropdown.pack()


radius_label = tk.Label(shapeareawin, text="Radius:", bg='#49494a', fg='white')
radius_entry = tk.Entry(shapeareawin)

length_label = tk.Label(shapeareawin, text="Length:", bg='#49494a', fg='white')
length_entry = tk.Entry(shapeareawin)
width_label = tk.Label(shapeareawin, text="Width:", bg='#49494a', fg='white')
width_entry = tk.Entry(shapeareawin)

base_label = tk.Label(shapeareawin, text="Base:", bg='#49494a', fg='white')
base_entry = tk.Entry(shapeareawin)
height_label = tk.Label(shapeareawin, text="Height:", bg='#49494a', fg='white')
height_entry = tk.Entry(shapeareawin)

#button to calculate shape area
calculate_button = tk.Button(shapeareawin, text="Calculate Area", command=calculate_area, bg='orange')

#displays area result
area_result = tk.Label(shapeareawin, text="Area:", bg='#49494a', fg='white', pady=10)

def update_widgets(*args):
    shape_type = shape_choice.get()
    clear_widgets()

    if shape_type == "Circle":
        radius_label.pack()
        radius_entry.pack()
    elif shape_type == "Rectangle":
        length_label.pack()
        length_entry.pack()
        width_label.pack()
        width_entry.pack()
    elif shape_type == "Triangle":
        base_label.pack()
        base_entry.pack()
        height_label.pack()
        height_entry.pack()

    calculate_button.pack(pady=10)
    area_result.pack()

shape_choice.trace("w", update_widgets)

def clear_widgets():
    for widget in [
        radius_label, radius_entry, length_label, length_entry,
        width_label, width_entry, base_label, base_entry,
        height_label, height_entry, calculate_button, area_result
    ]:
        widget.pack_forget()


shapeareawin.mainloop()