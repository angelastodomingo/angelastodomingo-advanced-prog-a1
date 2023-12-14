### Exercise 2 b: Square Grid ☑️ 	
#- With	the	pack	layout	manager, Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame
#- Using Pack() align  A and C at the top and B and D at the bottom of the frames that contain them
#- Support	resizing. Use	the	‘expand’ and	‘fill’ attributes	of	the	pack	method	to	make	the	labels	grow	and	expand	into	the	available	space.
#- Assign border value as 5 to the frames

from tkinter import * 
import random

app = Tk()  
app.title("Square Grid")

left_frame = Frame(app, 
                   bd=5, 
                   relief=GROOVE, 
                   width=200, 
                   height=200)

right_frame = Frame(app, 
                    bd=5, 
                    relief=GROOVE, 
                    width=200, 
                    height=200)

bA = Label(left_frame, 
           text="A", 
           width=20, 
           height= 6, 
           bg='#312e52',
           fg='white')

bB = Label(left_frame, 
           text="B", 
           width=20, 
           height= 6, 
           bg='white')

bC = Label(right_frame, 
           text="C", 
           width=20, 
           height= 6, 
           bg='white')

bD = Label(right_frame, 
           text="D", 
           width=20, 
           height= 6, 
           bg='#312e52',
           fg='white')

bA.pack(side='top', 
        fill=BOTH, 
        expand=True)

bB.pack(side='bottom', 
        fill=BOTH, 
        expand=True)

bD.pack(side='bottom', 
        fill=BOTH, 
        expand=True)

bC.pack(side='top', 
        fill=BOTH, 
        expand=True)

left_frame.pack(side='left', 
                expand=True, 
                fill='both')

right_frame.pack(side='right', 
                 expand=True, 
                 fill='both')

app.mainloop()

