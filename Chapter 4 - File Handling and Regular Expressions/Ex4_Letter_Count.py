### Exercise 4: letter count ☑️ 

#Develop a GUI App that asks the user to enter a character, reads the contents of the ```sentences.txt``` file, and counts the occurrences of the letter.

import tkinter as tk

class LetterCounter:
    def __init__(self, master):
        self.master = master
        self.master.title("Letter Count")

        #label widget 
        self.label = tk.Label(master, text="Enter a word or sentence:",bg='#49494a', fg='white')
        self.label.pack()
        
        #entry box for user inputs
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        #will display the result when user presses the button 
        self.result_label = tk.Label(master, text="",bg='#49494a', fg='white')
        self.result_label.pack()
        
        #button for user to press to find the number of occurences of the word/sentence the user has entered 
        self.count_button = tk.Button(master, text="Count Occurrences", command=self.count_occurrences, bg='gold')
        self.count_button.pack()

    #defined the function to search the contents of sentences.txt, and display the number of occurences of the word the user has typed in
    def count_occurrences(self):
        char_to_count = self.entry.get().lower()
        file_path = "sentences.txt" 
        try:
            with open(file_path, 'r') as file:  #finds sentences.txt in the directory
                content = file.read().lower()
                count = content.count(char_to_count)
                self.result_label.config(text=f"Occurrences of '{char_to_count}' in the file: {count}",bg='#49494a', fg='white')
        except FileNotFoundError:
            self.result_label.config(text="File not found.",bg='#49494a', fg='white')

#main window
if __name__ == "__main__":
    lettercount = tk.Tk()
    app = LetterCounter(lettercount)
    lettercount.geometry('300x100')
    lettercount.configure(bg='#49494a')
    lettercount.mainloop()
