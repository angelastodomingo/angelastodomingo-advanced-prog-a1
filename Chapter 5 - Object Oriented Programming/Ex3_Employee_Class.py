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
    def __int__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.age = ""

    def setData(self, name, position, salary, id):
        self.name = name
        self.position = position
        self.salary = salary 
        self.id = id

    def getData(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, ID: {self.id}"

class Employee_GUI(tk, Tk):
    def __int__(self):
        super().__int__()
        self.title("Employees details")
        self.geometry("400*400")
        self.employees = []
        self.add_employee()

    def add_employee(self):
        for _ in range(5):
            name = input("Enter name: ")
            position = input("Enter the position: ")
            salary = float(input("Emter the salary: "))
            id = input("Enter ID: ")
        employee = Employee()
        employee.setData(name, position, salary, id)
        self.employee.append(employee)
    self.display.employees()

    def display_employees(self):
        for employee in self.employees:
            print(employee.getData())
app = Employee_GUI()
app.mainloop()







