### Exercise 2: Student Class ☑️
#Develop a GUI using Tkinter to Create a class called Students.
#- The class should have the following members.```Name (string), Mark1 (int), Mark2 (int), Mark3 (int) ``` 
#- The class should have the following methods
#```calcGrade()``` - should return an average from the three marks.```display()```- should output the student name and calculated grade average
#- Create one object using a constructor that contains parameters to initialize all of the variables
#- Ask user to input the variable values using input() and pass the values to the second object

import tkinter as tk

#defines class name
class Students:
    def __init__(self, name, mark1, mark2, mark3): 
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self): #calculates the average grade of the student 
        return (self.mark1 + self.mark2 + self.mark3) / 3

    #calls calcgrade to calculate the average grade, then displays the result.
    def display(self):
        average = self.calcGrade()
        return f"Name: {self.name}\nAverage Grade: {average}"

#retrieves data 
def create_student():
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())

    student = Students(name, mark1, mark2, mark3)

    student_info_label.config(text=student.display())


studentwin = tk.Tk()
studentwin.title("Student Class")
studentwin.geometry('300x300')
studentwin.configure(bg='#49494a')

#labels and entry boxes
name_label = tk.Label(studentwin, text="Name:", bg='#49494a', fg='white')
name_label.pack()
name_entry = tk.Entry(studentwin)
name_entry.pack()

mark1_label = tk.Label(studentwin, text="Mark 1:", bg='#49494a', fg='white')
mark1_label.pack()
mark1_entry = tk.Entry(studentwin)
mark1_entry.pack()

mark2_label = tk.Label(studentwin, text="Mark 2:", bg='#49494a', fg='white')
mark2_label.pack()
mark2_entry = tk.Entry(studentwin)
mark2_entry.pack()

mark3_label = tk.Label(studentwin, text="Mark 3:", bg='#49494a', fg='white')
mark3_label.pack()
mark3_entry = tk.Entry(studentwin)
mark3_entry.pack()

#button to display info
create_button = tk.Button(studentwin, text="Create Student", command=create_student, bg='coral')
create_button.pack(pady=10)

student_info_label = tk.Label(studentwin, text="", bg='#49494a', fg='white')
student_info_label.pack()


studentwin.mainloop()