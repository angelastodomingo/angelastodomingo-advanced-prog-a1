#Create a GUI with 4 labels using the pack() geometry as shown in the below images. The	first image on the left shows	the	original display and the	second image on right shows	what	happens	when	the	window	is	resized.

#![image](https://github.com/a-subhani/CodeLab-II-Python-2023/assets/70882239/961eccd9-0750-4fd5-b553-421e4d0b8d7e)   &nbsp;&nbsp;&nbsp;    ![image](https://github.com/a-subhani/CodeLab-II-Python-2023/assets/70882239/53b0d1f2-b58d-4709-8d5b-ad8b0c908ba8)

#### Additional information
#Arguments values for many widgets, including Frames for Borders and Background 
#- bd is used for border width. For example bd=5
#- Relief is used for border-style values are FLAT, RAISED, GROOVE, SUNKEN, and RIDGE. For example relief=RAISED
#- bg is used for background color.For example bg="white" or bg="#FFFFFF".

#Pack arguments
#- Fill: Fill the space with the widget, Values are  Y, X, BOTH. For example fill=Y
#- Expand: The size of the button is expanded if the window is maximized. Values are 0,1, any number, YES, NO. For example  expand=0 (default) no expansion

from tkinter import * 
import random

app = Tk() 
app.title("Using pack")

bA = Label (app, text = "A", width= 12, bg = 'red', relief = GROOVE, bd = 5)
bB = Label (app, text = "B", width= 12, bg = 'yellow')
bC = Label (app, text = "C", width= 12, bg = 'blue')
bD = Label (app, text = "D", width= 12, bg = 'white')

bA.pack(side = 'top', fill = X, expand = 1)
bB.pack(side = 'bottom')
bD.pack(side='right', fill=Y)
bC.pack(side='top', anchor='n')


app.mainloop()

