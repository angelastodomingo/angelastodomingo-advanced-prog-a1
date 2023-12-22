### Exercise 5: Playing around in class ☑️
#Use this exercise to play around with creating and accessing class members and methods. Develop a GUI using Tkinter to Create a class called Animal
#- Give the class at least the following members  ```Type, Name, Colour, Age, Weight, Noise```
#- The class should have the following methods
#```sayHello()``` - says its name via print,```makeNoise()``` -make an appropriate noise via print, ```animalDetails()``` -output all the details of the animal object
#- Instantiate at least two objects from your animal class (e.g. Dog, Cow)
#- Set values for each of the variables
#- Invoke each of the class functions

import tkinter as tk

class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        self.Type = animal_type #animal species 
        self.Name = name #animal name 
        self.Colour = color #animal coat color 
        self.Age = age #animal age 
        self.Weight = weight #animal weight 
        self.Noise = noise #animal sound 

    #details of dog and cow 
    def animalDetails(self):
        details = (
            f"Type: {self.Type}\n"
            f"Name: {self.Name}\n"
            f"Colour: {self.Colour}\n"
            f"Age: {self.Age}\n"
            f"Weight: {self.Weight}\n"
            f"Noise: {self.Noise}"
        )
        print(details)

#dog n cow
dog = Animal("Dog", "Buddy", "Brown", 4, 20, "Bark")
cow = Animal("Cow", "Daisy", "White", 6, 600, "Moo")

#class functions
dog.animalDetails()
print("\n")
cow.animalDetails()

#gui 
playwin = tk.Tk()
playwin.title("Playing around in class")
playwin.geometry('300x300')

result_text = tk.Text(playwin, height=30, width=40)
result_text.pack()

result_text.insert("1.0", "Animal 1 Information:\n") #inserts animal 1 info. 
result_text.insert("end", f"Type: {dog.Type}\n")
result_text.insert("end", f"Name: {dog.Name}\n")
result_text.insert("end", f"Colour: {dog.Colour}\n")
result_text.insert("end", f"Age: {dog.Age}\n")
result_text.insert("end", f"Weight: {dog.Weight}\n")
result_text.insert("end", f"Noise: {dog.Noise}\n\n")

result_text.insert("end", "Animal 2 Information:\n") #inserts animal 2 info.
result_text.insert("end", f"Type: {cow.Type}\n")
result_text.insert("end", f"Name: {cow.Name}\n")
result_text.insert("end", f"Colour: {cow.Colour}\n")
result_text.insert("end", f"Age: {cow.Age}\n")
result_text.insert("end", f"Weight: {cow.Weight}\n")
result_text.insert("end", f"Noise: {cow.Noise}\n")

result_text.config(state="disabled") #text will only be read-only 

playwin.mainloop()