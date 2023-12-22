### Exercise 1: Greeting App ☑️
#Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.

#In InputFrame, include the following:
#- A title label in blue.
#- An entry field for the user's name.
#- A dropdown menu for selecting a color.
#- An "Update Greeting" button.
#- In DisplayFrame, include a label to display the personalized greeting.
#- Initially, DisplayFrame is empty, when the user clicks the "Update Greeting" button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.

#Use different background colors for each frame.

import tkinter as tk
from tkinter import ttk

greeting = tk.Tk()
greeting.title("Greeting App")
greeting.geometry("400x400")

#greets the user 
startinglabel = tk.Label(greeting, text="Greetings! Write your name:", bg = 'blue', fg= "white", pady=5, padx=10)
startinglabel.pack(anchor='w', pady=50, padx=40)

#entry box for user to type in their name
name = tk.Entry(greeting, font=('Arial', 10), width=40, justify='left') 
name.place(x=40, y=85, width=300, height=60) #makes the entry box a bit larger

colorlabel = tk.Label(greeting, text="Please select a color:")
colorlabel.pack(anchor='w', pady=(25,10), padx=40) #adds padding between entry box and 'update button' button.

#to display results when the user clicks the button
def on_click():
    color_picked = color_selected.get()
    username = name.get()
    
    result = tk.Label(greeting, text=f"Hello, {username}! It is good to see you.", fg=color_picked)
    result.pack()
    
#dropdown list of colors 
dropdown_list = ["red", "green", "blue", "magenta", "cyan", "yellow", "purple", "firebrick", "saddlebrown", "hotpink"]


#Combobox
color_selected = ttk.Combobox(greeting, values=dropdown_list)
color_selected.pack(side= tk.TOP, anchor='nw', padx=40)

#Button for update
button = tk.Button(greeting, text="Update Greeting", command=on_click, padx=30)
button.pack(anchor='w', padx=100, pady=10)

greeting.mainloop()