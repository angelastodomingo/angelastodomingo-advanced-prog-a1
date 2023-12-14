### Exercise 1: User information ☑️ 
#Develop a GUI App to create a file called ```bio.txt``` and write the following information to the file asking user to enter the values:
#Name
#Age
#Hometown
#Each piece of data should be on a new line
#Once the data has been written to the file, read the data from the file and output the data.

import tkinter as tk
from tkinter import ttk


def write_to_file(): #to write data to file
    name = name_entry.get()
    age = age_entry.get()
    hometown = hometown_entry.get()

    with open("bio.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hometown: {hometown}\n")

    result_label.config(text="Data has been written to bio.txt")

#to read and display info from file
def read_from_file():
    try:
        with open("bio.txt", "r") as file:
            data = file.read()
            result_label.config(text=data)
    except FileNotFoundError:
        result_label.config(text="bio.txt not found")

userwin = tk.Tk()
userwin.title("User Information")

#forms to collect user info
form_frame = ttk.LabelFrame(userwin, text="Enter User Information")
form_frame.grid(row=0, column=0, padx=10, pady=10)

name_label = ttk.Label(form_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = ttk.Label(form_frame, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = ttk.Entry(form_frame)
age_entry.grid(row=1, column=1, padx=10, pady=5)

hometown_label = ttk.Label(form_frame, text="Hometown:")
hometown_label.grid(row=2, column=0, padx=10, pady=5)
hometown_entry = ttk.Entry(form_frame)
hometown_entry.grid(row=2, column=1, padx=10, pady=5)

write_button = ttk.Button(userwin, text="Write to File", command=write_to_file)
write_button.grid(row=1, column=0, padx=10, pady=10)

read_button = ttk.Button(userwin, text="Read from File", command=read_from_file)
read_button.grid(row=2, column=0, padx=10, pady=10)

result_label = ttk.Label(userwin, text="")
result_label.grid(row=3, column=0, padx=10, pady=5)

userwin.mainloop()