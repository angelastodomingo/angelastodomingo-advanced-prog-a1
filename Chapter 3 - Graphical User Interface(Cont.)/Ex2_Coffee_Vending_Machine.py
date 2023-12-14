### Exercise 2: Coffee Vending Machine☑️
#Develop a coffee Vending Machine that asks users to select the type of coffee, and also prompts users to select various options like sugar, milk, etc. Once selected display the message using a message box. Also, use images in the app.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


def make_coffee(): #to display options and message
    coffee_type = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()

    message = f"Enjoy your {coffee_type} coffee!"
    if sugar:
        message += " With sugar."
    if milk:
        message += " And milk."

    messagebox.showinfo("Coffee Dispenser", message)


coffee = tk.Tk()
coffee.title("Coffee Vending Machine")


#coffee choices
coffee_var = tk.StringVar()
coffee_var.set("Espresso")  
coffee_label = ttk.Label(coffee, text="Select Coffee:")
coffee_menu = ttk.Combobox(coffee, textvariable=coffee_var, values=["Espresso", "Cappuccino", "Latte", "Mocha"]) #creates a drop down menu

#sugar box
sugar_var = tk.BooleanVar()
sugar_check = ttk.Checkbutton(coffee, text="Add Sugar", variable=sugar_var)

#milk box
milk_var = tk.BooleanVar()
milk_check = ttk.Checkbutton(coffee, text="Add Milk", variable=milk_var)

#coffee pics
coffee_images = {
    "Espresso": "espresso.jpg"
}

#displays coffee pic
def display_coffee_image():
    selected_coffee = coffee_var.get()
    image_path = coffee_images.get(selected_coffee, "default.jpg")
    img = Image.open(image_path)
    img = img.resize((300, 200))
    photo = ImageTk.PhotoImage(img)
    image_label.configure(image=photo)
    image_label.image = photo

#button to make coffee
dispense_button = ttk.Button(coffee, text="Make coffee", command=make_coffee)
image_label = ttk.Label(coffee, image=None)

#layout
coffee_label.grid(row=0, column=0, padx=10, pady=10)
coffee_menu.grid(row=0, column=1, padx=10, pady=10)
sugar_check.grid(row=1, column=0, padx=10, pady=10)
milk_check.grid(row=1, column=1, padx=10, pady=10)
image_label.grid(row=2, column=0, columnspan=2)
dispense_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#to actually display the coffee image 
display_coffee_image()

coffee.mainloop()
