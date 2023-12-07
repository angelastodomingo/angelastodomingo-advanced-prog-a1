### Exercise 1: Woof Woof ☑️
 
#Develop a GUI using Tkinter with a class that defines the characteristics of a dog. The program should instantiate two objects from this class and assign data to its members.
#The program should then output the data from each object and the oldest dog should woof via a class method.

import tkinter as tkinter
class Dog:
    def __int__(self, name, age):
        self.name = name
        self.age = age 

    def woof(self):
        return f"{self.name}, says woof"
dog1 = Dog("German Shepherd", 10)
dog2 = Dog("Husky, 8")
older_dog = dog1 if dog1.age>dog2.age else dog2 

class DogGUI(tk, Tk):
    def __int__(self):
        super().__init__()
        self.title("Dog Info")
        self.geometry(400*400)
        self.display_dog_info()
    def display_dog_info(self):
        label1 = tk.Label(self, "Dog1: {dog1.name}, {dog1.age} years old")
        label1.pack()
        label2 = tk.Label(self, "Dog1: {dog1.name}, {dog1.age} years old")
        label2.pack()
        older_dog_label = tk.label(self, text = f"the oldest dog is {older_dog}")
        older_dog_label.pack()
        woof_button = tk.button(self, text = "make woof")
        woof_button.pack()

    def woof(self):
        result = oldest_dog.woof()
        woof_label= tk.Label(self, text = result)
        woof_label.pack()
app = DogGUI()
app.mainloop()