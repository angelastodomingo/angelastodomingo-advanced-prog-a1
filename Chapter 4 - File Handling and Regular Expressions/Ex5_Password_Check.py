## Exercise 5: Password Check ☑️ 

#Develop a GUI App to check the validity of a password given by the user in the entry widget. The password should satisfy the following criteria: 
#- Contain at least 1 letter between a and z 
#- Contain at least 1 number between 0 and 9 
#- Contain at least 1 letter between A and Z
#- Contain at least 1 character from $, #, @ 
#- Minimum length of password: 6 
#- Maximum length of password: 12

#Ask user to include a maximum of 5 passcode attempts. Each time the user enters an incorrect passcode, they should be prompted of how many passcode attempts remain. If there are 5 failed passcode attempts the while loop should break and inform the user that the authorities have been alerted!

import tkinter as tk
from tkinter import messagebox


def check_password():
    password = password_entry.get()

    # Define the password criteria
    criteria = [
        any(c.islower() for c in password),  #at least 1 lowercase letter
        any(c.isdigit() for c in password),  #at least 1 digit
        any(c.isupper() for c in password),  #at least 1 uppercase letter
        any(c in "$#@ " for c in password),   #at least 1 of $, #, or @
        6 <= len(password) <= 12  #minimum and maximum length
    ]

    if all(criteria):
        result_label.config(text="Password is valid!")
    else:
        if not attempts_remaining:
            result_label.config(text="The authorities have been alerted!")
        else:
            result_label.config(
                text=f"Invalid password. {attempts_remaining} attempts remaining."
            )
            password_entry.delete(0, "end")
            attempts_remaining[0] -= 1


passwordwin = tk.Tk()
passwordwin.title("Password Check")
passwordwin.geometry('300x100')

attempts_remaining = [5]

#label and entry boxes
password_label = tk.Label(passwordwin, text="Enter a password:")
password_label.pack()
password_entry = tk.Entry(passwordwin, show="*")  # Show * for password input
password_entry.pack()

#button to validate password
validate_button = tk.Button(passwordwin, text="Validate Password", command=check_password)
validate_button.pack(pady=10)

#displays result
result_label = tk.Label(passwordwin, text="")
result_label.pack()


passwordwin.mainloop()