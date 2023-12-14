### Exercise 1: Woof Woof ☑️
 
#Develop a GUI using Tkinter with a class that defines the characteristics of a dog. The program should instantiate two objects from this class and assign data to its members.
#The program should then output the data from each object and the oldest dog should woof via a class method.

import tkinter as tk

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def woof(self):
        return f"{self.name} says Woof!"


def display_dog_info(): #to get dog info
    dog1_name = name_entry1.get()
    dog1_age = int(age_entry1.get())
    dog2_name = name_entry2.get()
    dog2_age = int(age_entry2.get())

    dog1 = Dog(dog1_name, dog1_age)
    dog2 = Dog(dog2_name, dog2_age)

    dog_info_label.config(text=f"{dog1.name} is {dog1.age} years old.\n{dog2.name} is {dog2.age} years old.", bg='#49494a', fg='white')

    oldest_dog = max(dog1, dog2, key=lambda dog: dog.age)
    woof_label.config(text=oldest_dog.woof())

dog = tk.Tk()
dog.title("Woof woof")
dog.geometry('300x300')
dog.configure(bg='#49494a')

#labels and entry boxes
name_label1 = tk.Label(dog, text="Dog 1 Name:", bg='#49494a', fg='white')
name_label1.pack()
name_entry1 = tk.Entry(dog)
name_entry1.pack()

age_label1 = tk.Label(dog, text="Dog 1 Age:", bg='#49494a', fg='white')
age_label1.pack()
age_entry1 = tk.Entry(dog)
age_entry1.pack()

name_label2 = tk.Label(dog, text="Dog 2 Name:", bg='#49494a', fg='white')
name_label2.pack()
name_entry2 = tk.Entry(dog)
name_entry2.pack()

age_label2 = tk.Label(dog, text="Dog 2 Age:", bg='#49494a', fg='white')
age_label2.pack()
age_entry2 = tk.Entry(dog)
age_entry2.pack()

#button for dog info
display_button = tk.Button(dog, text="Display Dog Info", command=display_dog_info, bg='mediumspringgreen')
display_button.pack(pady=10)


dog_info_label = tk.Label(dog, text="", bg='#49494a', fg='white')
dog_info_label.pack()

woof_label = tk.Label(dog, text="",bg='#49494a', fg='white')
woof_label.pack()

# Start the main loop
dog.mainloop()