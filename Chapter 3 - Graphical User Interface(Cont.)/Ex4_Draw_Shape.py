## Exercise 4: Draw Shape☑️
#Using tkinter module develop Gui to ask the user to select shapes like oval, rectangle, square, and triangle and draw the shape using canvas.

import tkinter as tk
from tkinter import ttk


def draw_shape(): #to draw shapes on the canvas
    selected_shape = shape_var.get()
    canvas.delete("all")  # Clear the canvas

    if selected_shape == "Oval":
        canvas.create_oval(50, 50, 200, 150, fill="mediumorchid")
    elif selected_shape == "Rectangle":
        canvas.create_rectangle(50, 50, 200, 150, fill="lightgreen")
    elif selected_shape == "Square":
        canvas.create_rectangle(50, 50, 150, 150, fill="firebrick")
    elif selected_shape == "Triangle":
        canvas.create_polygon(50, 150, 125, 50, 200, 150, fill="skyblue")

shape = tk.Tk()
shape.title("Draw Shape")

shapelabel = ttk.Label(shape, text="Select a shape:")
shapelabel.pack(pady=10)


shapes = ["Oval", "Rectangle", "Square", "Triangle"] #drop down menu to select shapes 
shape_var = tk.StringVar()
shape_menu = ttk.Combobox(shape, textvariable=shape_var, values=shapes)
shape_menu.pack()

#button to draw shapes
draw_button = ttk.Button(shape, text="Draw Shape", command=draw_shape)
draw_button.pack(pady=10)

#canvas. it's like paper
canvas = tk.Canvas(shape, width=300, height=200, background="white")
canvas.pack()

shape.mainloop()