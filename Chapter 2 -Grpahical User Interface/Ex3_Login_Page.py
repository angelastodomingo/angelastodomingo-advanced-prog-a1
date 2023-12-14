## Exercise 3: Login page ☑️ 

#Create a login page using the Grid geometry. 

from tkinter import *
page = Tk()
page.title("Login Page")
page.geometry('500x500')
page.configure(bg='#333333') #window color

#Labels
username_label = Label(page, 
                       text="Username:", 
                       bg='#333333', #changed the background of the text to match the window background color 
                       fg='white', #font color
                        font=('Arial', 15,))


password_label = Label(page, 
                       text="Password:", 
                       bg='#333333',
                       fg='white',
                       font=('Arial', 15,))

#Entry Widgets
username_entry = Entry(page, font=('Arial', 12,))
password_entry = Entry(page, show="*", font=('Arial', 12,)) #It'll display as asterisks for the password

#Login Button
login_button = Button(page, 
                      text="Login", 
                      bg= '#c2e36d',
                      fg='black',
                      font=('Arial', 10,))

#Grid layout
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=3, column=0, columnspan=10) #positions the login button in the middle

page.mainloop()
