### Exercise 2: CountString ☑️ 
#The file ```sentences.txt``` has a list of string data. Develop a GUI App that finds out how many times the following string appears 

#- Hello my name is Peter Parker
#- I love Python Programming
#- Love
#- Enemy

import tkinter as tk

class StringCounter: #defined class
    def __init__(self, master): 
        self.master = master #the parameter of the main window
        self.master.title("Count String") #sets the title of the main window 

        
        self.strings_to_count = [ #will be used to count occurences of the 4 sentences
            "Hello my name is Peter Parker",
            "I love Python Programming",
            "Love",
            "Enemy"
        ]
        #stylization 
        self.result_label = tk.Label(master, text="",bg='#49494a', fg='white')
        self.result_label.pack()

        self.count_button = tk.Button(master, text="Count Occurrences", command=self.count_occurrences, bg='dodgerblue', fg='white')
        self.count_button.pack()

    def count_occurrences(self):
        file_path = "sentences.txt"  #finds sentences.txt in directory
        try:
            with open(file_path, 'r') as file:
                content = file.read().lower()
                counts = [content.count(s.lower()) for s in self.strings_to_count]
                
                result_text = "\n".join([f"{string}: {count}" for string, count in zip(self.strings_to_count, counts)])
                self.result_label.config(text=result_text)
        except FileNotFoundError:
            self.result_label.config(text="File not found.") #will display if sentences.txt isn't found in the directory
            
#the main window.
if __name__ == "__main__":
    countstring = tk.Tk()
    root = StringCounter(countstring)
    countstring.geometry('300x150')
    countstring.configure(bg='#49494a')
    countstring.mainloop()
