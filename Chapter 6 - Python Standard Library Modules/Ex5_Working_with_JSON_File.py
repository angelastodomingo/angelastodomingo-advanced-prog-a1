## Exercise 4: Working with JSON File ☑️
#Create a JSON file named 'StudentJson.json' with the following details
#1. Ask the user to enter the student name, ID, and course and write these contents to the JSON file.
#2.Read the contents from the JSON file and display the individual values.  
#  Expected Output :
#  ```
#  Details of the Student are
# 		Name: Alpha
# 		ID: 1
# 		course: BSc CC
#```
#3. Append another dictionary as follows as key value pair for student 1 in StudentDetails dictionary to form a nested dictionay. Later update the JSON file.
#```
# "CourseDetails":{ 
#             		 "Group": "A",
 #            		 "Year": 2
#		}
#```
#4. Print the individual vlaues of the Student details reading from JSON file.

#  Expected Output :
#```
#Details of the Student are
#		  Name: Alpha
#		  ID: 1
# 		 course: BSc CC
# 		 Group: A
# 		 Year: 2
#```

import json


def get_student_details(): #gets user input for details
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    course = input("Enter student course: ")
    return {"Name": name, "ID": student_id, "course": course}


def read_and_display_details(file_path): #displays info to file
    with open(file_path, "r") as file:
        student_details = json.load(file)
        print("Details of the Student are")
        print(f"\tName: {student_details['Name']}")
        print(f"\tID: {student_details['ID']}")
        print(f"\tcourse: {student_details['course']}")
        if 'CourseDetails' in student_details:
            print(f"\tGroup: {student_details['CourseDetails']['Group']}")
            print(f"\tYear: {student_details['CourseDetails']['Year']}")


def append_and_update(file_path, new_data): #updates JSON file
    try:
        with open(file_path, "r") as file:
            student_details = json.load(file)
        
        
        student_details.update(new_data)
        
        with open(file_path, "w") as file:
            #updates contents of JSON file
            json.dump(student_details, file, indent=4)
            
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

#gets user input for JSON file
user_data = get_student_details()
with open('StudentJson.json', 'w') as file:
    json.dump(user_data, file, indent=4)

#display info from JSON file
read_and_display_details('StudentJson.json')

#update JSON file with course details
new_data = {"CourseDetails": {"Group": "A", "Year": 2}}
append_and_update('StudentJson.json', new_data)

#displays updated JSON file info
read_and_display_details('StudentJson.json')