#Develop a GUI program to do the following using the tkinter module
#- create a label to display the welcome message and change the label font style (font name, bold, size)
#- Set the default window size
#- Disable resizing the window
#- Add background color to the Window.

from tkinter import * 

window = Tk()
window.geometry("500x300")
window.title("Welcome")

label = Label(window, 
            text = "Welcome to my first GUI!",
            font=('Arial', 30, 'bold'),
            bg= '#ff7a91',
            fg='white')

label.pack()
window.config(background="#ff7a91") #changes background color of the window 
window.resizable(0,0) #Disables resizing the window 
window.mainloop()






