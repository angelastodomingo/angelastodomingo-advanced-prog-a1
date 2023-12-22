## Exercise 3: Area Function☑️
#Develop a GUI application using tkinter that allows users to calculate and display the areas of various shapes, including circles, squares, and rectangles. The application should utilize a tabbed interface to organize the calculations for each shape.
#Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.

import tkinter as tk
from tkinter import ttk
import math

#calculates area of circle
def calculate_circle_area():
    radius = float(circle_radius_entry.get())
    area = math.pi * (radius**2)
    circle_result_label.config(text=f"Area of Circle: {area:.2f} square units")

#calculates area of square
def calculate_square_area():
    side_length = float(square_side_entry.get())
    area = side_length**2
    square_result_label.config(text=f"Area of Square: {area} square units")

#calculates area of rectangle 
def calculate_rectangle_area():
    length = float(rectangle_length_entry.get())
    width = float(rectangle_width_entry.get())
    area = length * width
    rectangle_result_label.config(text=f"Area of Rectangle: {area} square units")


area = tk.Tk()
area.title("Area Function")

#notebook creates tabs 
notebook = ttk.Notebook(area)

#different tabs for each shape
circle_frame = ttk.Frame(notebook)
square_frame = ttk.Frame(notebook)
rectangle_frame = ttk.Frame(notebook)

#creates tabs for circle, square and rectangle.
notebook.add(circle_frame, text="Circle") 
notebook.add(square_frame, text="Square")
notebook.add(rectangle_frame, text="Rectangle")

notebook.pack(padx=10, pady=10, fill="both", expand=True)

#circle tab widgets
circle_radius_label = ttk.Label(circle_frame, text="Enter the radius:")
circle_radius_entry = ttk.Entry(circle_frame)
calculate_circle_button = ttk.Button(circle_frame, text="Calculate", command=calculate_circle_area)
circle_result_label = ttk.Label(circle_frame, text="")

#circle tab positions
circle_radius_label.grid(row=0, column=0, padx=10, pady=10)
circle_radius_entry.grid(row=0, column=1, padx=10, pady=10)
calculate_circle_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
circle_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#square tab widgets
square_side_label = ttk.Label(square_frame, text="Enter the side length:")
square_side_entry = ttk.Entry(square_frame)
calculate_square_button = ttk.Button(square_frame, text="Calculate", command=calculate_square_area)
square_result_label = ttk.Label(square_frame, text="")

#square tab positions
square_side_label.grid(row=0, column=0, padx=10, pady=10)
square_side_entry.grid(row=0, column=1, padx=10, pady=10)
calculate_square_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
square_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#rectangle tab widgets 
rectangle_length_label = ttk.Label(rectangle_frame, text="Enter the length:")
rectangle_length_entry = ttk.Entry(rectangle_frame)
rectangle_width_label = ttk.Label(rectangle_frame, text="Enter the width:")
rectangle_width_entry = ttk.Entry(rectangle_frame)
calculate_rectangle_button = ttk.Button(rectangle_frame, text="Calculate", command=calculate_rectangle_area)
rectangle_result_label = ttk.Label(rectangle_frame, text="")

#rectangle tab positions 
rectangle_length_label.grid(row=0, column=0, padx=10, pady=10)
rectangle_length_entry.grid(row=0, column=1, padx=10, pady=10)
rectangle_width_label.grid(row=1, column=0, padx=10, pady=10)
rectangle_width_entry.grid(row=1, column=1, padx=10, pady=10)
calculate_rectangle_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
rectangle_result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


area.mainloop()