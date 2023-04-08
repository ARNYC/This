'''
Display a menu to the user about the actions s/he can perform: 
add note, scroll, modify a note, search, quit  
Ask them their choice
Based on the chosen option, perform the action

question; I am assuming that import notebook automatically executes 
import note, so we do not have to import it separately
'''
from notebook import Notebook 

import sys
class App:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            1: self.add_note,
            2: self.show_notes,
            3: self.modify_note,
            4: self.search_note,
            5: self.quit
        }

    def run(self):
        while True:
            self.display_menu()
            # read user choice
            selection = int(input("Input your Choice:"))
            action = self.choices[selection]
            if action:
                action()
            else:
                print("Invalid choice!")
            # execute

    def display_menu(self):
        print("Notebook Menu:")
        print("1. Add note")
        print("2. See all notes")
        print("3. Modify note")
        print("4. Search notes ")
        print("5. Quit")
    

    def add_note(self):
        memo = input("enter memo for note:")
        tags = input("Enter tags separated by commas:").split(',')
        self.notebook.add_note(memo, tags)
        print("Note added ")


    def show_notes(self):
        self.notebook.scroll()

    def modify_note(self):
            while True:
                try:
                    id = int(input('Input note Id to be modified or enter 0 to quit: '))
                    break
                except ValueError:
                    print("Must enter a number greater than 0")
            if id > 0:
                memo = input('Type in new memo or Press enter ')
                tags = input('Type in tags separated by comma or Press enter ').split(',')
                if memo  or tags :
                    self.notebook.modify_note(id,memo,tags)

    def search_note(self):
        s_term = input("Enter the term to find in notes: " )
        matching_notes = self.notebook.search_notes(s_term)
        print (f"Note Id#s containing {s_term}:", matching_notes)


    def quit(self):
        print("Thanks for using the notebook app!")
        sys.exit(0)

if __name__ == "__main__":
    App().run()


