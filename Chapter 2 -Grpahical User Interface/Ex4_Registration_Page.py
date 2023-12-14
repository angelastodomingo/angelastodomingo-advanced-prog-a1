## Exercise 4: Registration page ☑️
#Using widgets create a GUI as shown in below image  

#![Student Management System](https://github.com/a-subhani/CodeLab-II-Python-2023/assets/70882239/1115b29d-5491-4967-b164-80ba26355a56)

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

reg = tk.Tk()
reg.title("Registration Page")

#header
header_frame = ttk.Frame(reg)
header_frame.grid(row=0, column=0, columnspan=2)

#loads and resizes the logo
image = Image.open("logo.png")  
image = image.resize((400, 90))
banner_image = ImageTk.PhotoImage(image)

#aligns the header in the center
header_label = ttk.Label(header_frame, image=banner_image)
header_label.grid(row=0, column=0, columnspan=2)
header_label.image = banner_image

#title labels
title_label = ttk.Label(header_frame, text="Student Management System", font=("Helvetica", 16, 'bold'), foreground="#262940")
title_label.grid(row=1, column=0, columnspan=2)

title_label2 = ttk.Label(header_frame, text="New Student Registration", font=('Arial', 12, 'bold'), foreground="#262940")
title_label2.grid(row=20, column=0, columnspan=2, padx=10, pady=5)

#form
form = ttk.LabelFrame(reg)
form.grid(row=3, column=0, columnspan=2,)

#labels and the entry boxes
name = ttk.Label(form, text="Student Name:", font=('Courier', 10))
name.grid(row=0, column=0, padx=10, pady=5)

name_entry = ttk.Entry(form, background='#adaeb7')
name_entry.grid(row=0, column=1, padx=10, pady=5)

number = ttk.Label(form, text="Mobile Number:", font=('Courier', 10))
number.grid(row=1, column=0, padx=10, pady=5)

number_entry = ttk.Entry(form)
number_entry.grid(row=1, column=1, padx=10, pady=5)

email = ttk.Label(form, text="Email Id:", font=('Courier', 10))
email.grid(row=2, column=0, padx=10, pady=5)

email_entry = ttk.Entry(form)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address = ttk.Label(form, text="Home Address:", font=('Courier', 10))
address.grid(row=3, column=0, padx=10, pady=5)

address_entry = ttk.Entry(form)
address_entry.grid(row=3, column=1, padx=10, pady=5)

gender = ttk.Label(form, text="Gender:", font=('Courier', 10))
gender.grid(row=4, column=0, padx=10, pady=5)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(form, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combobox.grid(row=4, column=1, padx=10, pady=5)

#courses radiobuttons
course = ttk.Label(form, text="Courses Enrolled:", font=('Courier', 10))
course.grid(row=6, column=0, padx=10, pady=5)
course_var = tk.StringVar()
course_var.set("None")
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM",]
for i, course in enumerate(courses):
    course_radio = ttk.Radiobutton(form, text=course, variable=course_var, value=course)
    course_radio.grid(row=6+i, column=1, padx=10, pady=2)

#language checkboxes
languages_list = ttk.Label(form, text="Languages Known:", font=('Courier', 10))
languages_list.grid(row=10, column=0, padx=10, pady=5)
language_vars = [tk.BooleanVar() for _ in range(3)]
languages = ["English", "Tagalog", "Hindi/Urdu"]
for i, language in enumerate(languages):
    language_check = ttk.Checkbutton(form, text=language, variable=language_vars[i])
    language_check.grid(row=10+i, column=1, padx=10, pady=2)

#slider
communication_label = ttk.Label(form, text="Rate your English Communication Skills:", font=('Courier', 10, 'bold'))
communication_label.grid(row=13, column=0, columnspan=2, padx=10, pady=5)
communication_scale = ttk.Scale(form, from_=0, to=10, orient="horizontal")
communication_scale.grid(row=14, column=0, columnspan=2, padx=10, pady=5)

#buttons
submit_button = ttk.Button(reg, text="Submit")
submit_button.grid(row=15, column=0, padx=10, pady=10)

style = ttk.Style()
style.theme_use('clam')

#background color for the buttons 
style.map("TButton", background=[("active", "#22263d")])

style.configure("TButton", background="#22263d", font=("Courier", 10, "bold",), foreground="white")

clear_button = ttk.Button(reg, text="Clear", style="TButton")
clear_button.grid(row=15, column=1, padx=10, pady=10)



reg.mainloop()