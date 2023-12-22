### Exercise 3: Employee Class ☑️
#Develop a GUI using Tkinter to Create an employee class with the following members:
# ```name, age, id, salary```
#- Add the following methods:
#```setData()``` - should allow employee data to be set via user input,```getData()```- should output employee data to the console
#- Create a list of 5 employees. Ask the user to enter the details of 5 employees using the add_employee method and then display the output using the display_emloyee method as mentioned below
#Expected output:
#```			
#Name	Position	Salary	ID
#Alice	Manager		9500.0	1
#Bob	Accountant	6000.0	2
#Brain	Social Media	4000.0	3
#Frank	Salesman	2500.0	4
#Marker	Clerk		1500.0	5
#```

import tkinter as tk

class Employee:
    def __init__(self):
        self.name = "" #employee name 
        self.position = "" #employee job
        self.salary = 0.0 #employee salary
        self.id = 0 #employee id
        
    #4 parameters to set variables 
    def setData(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id
        
    #returns formatted employee data 
    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"


def add_employee(): #to create employee and add to list
    name = name_entry.get()
    position = position_entry.get()
    salary = float(salary_entry.get())
    emp_id = len(employees) + 1

    employee = Employee()
    employee.setData(name, position, salary, emp_id)
    employees.append(employee)

    name_entry.delete(0, "end")
    position_entry.delete(0, "end")
    salary_entry.delete(0, "end")

    if len(employees) == 5:
        add_button.config(state="disabled")

def display_employees(): #displays employee data
    result_text.config(state="normal")
    result_text.delete(1.0, "end")
    result_text.insert("end", "Name\tPosition\tSalary\tID\n")
    for employee in employees:
        result_text.insert("end", employee.getData() + "\n")
    result_text.config(state="disabled")


employeewin = tk.Tk()
employeewin.title("Employee Class")
employeewin.configure(bg='#49494a')

#labels and entry boxes
name_label = tk.Label(employeewin, text="Name:", bg='#49494a', fg='white')
name_label.pack()
name_entry = tk.Entry(employeewin)
name_entry.pack()

position_label = tk.Label(employeewin, text="Position:", bg='#49494a', fg='white')
position_label.pack()
position_entry = tk.Entry(employeewin)
position_entry.pack()

salary_label = tk.Label(employeewin, text="Salary:", bg='#49494a', fg='white')
salary_label.pack()
salary_entry = tk.Entry(employeewin)
salary_entry.pack()

#adds employees
add_button = tk.Button(employeewin, text="Add Employee", command=add_employee, bg='saddlebrown', fg='white')
add_button.pack(pady=10)

#displays employees
display_button = tk.Button(employeewin, text="Display Employees", command=display_employees, bg='chocolate', fg='white')
display_button.pack()

#employee data
result_text = tk.Text(employeewin, state="disabled", height=10, width=40)
result_text.pack()

#stores employees
employees = []

employeewin.mainloop()