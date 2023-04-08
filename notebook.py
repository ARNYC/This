# notebook is a searchable collection of notes 
# a user should be able to see a note given its id
# a note should be modifiable given its id (modify the memo or add more tags)
# ability to add a note 


# Build a class notebook which is a collection of notes
# Attributes: notes 
# Constructor/initializer
# Functionality
# add
# collection: mutable, indexed
# notes: list
from note import Note
'''
Functionality:
create
add note
modify a note given it's id
search 
'''
class Notebook:
    def __init__ (self, notes=[]):
        self.notes = notes  # it was []

    def add_note(self, memo,tags=[]):
        note = Note(memo,tags)  
        self.notes.append(note)
        print(type(note.tags))

    def show_notes(self, notes):
        for note in notes:
            note.show_note()
            print(type(note.tags))

    def scroll(self):
        # go through the notes 1 by 1
        # print them
        self.show_notes(self.notes)

    def show_note_by_id(self, id):
        print("shownote id",id)
        found = False
        for note in self.notes:
            if note.get_id() == id:
                found = True
                note.show_note()
        if not found:
            print("Invalid note id")
    
    def modify_note(self,id,memo='',tags=[]):
        print("modifying",id,memo,tags)
        # get the note by id
        # from a set of notes, get a note having the same id as the parameter id
        # going over the notes 1 by 1, check if the given note has the matching id
        found = False
        #for note in nb.notes: # tested this. Discuss in class
        for note in self.notes:
            
        #for note in self.notes:
            if note.get_id() == id:
                found = True
                if memo != '':
                    note.modify_memo(memo)
                    #note.memo = memo  
                if tags:
                    
                    print("notebook modify_note",type(tags),tags, type(note.tags),note.tags)  
                    note.add_tags(tags)
        if not found:
            print("Invalid note id:", id)
        # modify the note according to the new memo and the tags
    
    def search_notes(self, s_term):
        matching_notes = []
        for note in self.notes:
            if note.search_note(s_term):
                note.show_note() 
                matching_notes.append(note.get_id())
        if not matching_notes:
            print('No matching notes found!')
        return matching_notes         

        
#search by a term in memo and tags

# create nb
# create a couple of notes
# add them to the nb
# scroll through the nb
#nb = Notebook()
#nb.add_note('memo1',['tag1','tag2'])
# nb.add_note('memo2','tag3')
# nb.scroll()
# nb.show_note_by_id(2)

# nb.modify_note(2,'memo_r 2',['tags3r'])
# nb.show_note_by_id(2)

# nb.modify_note(5)

# nb.modify_note(2, 'home_loan')
# nb.show_note_by_id(2)

# nb.modify_note(2, tags=['xyz'])
# nb.show_note_by_id(2)

# nb.modify_note(2, 'Baloon_loan', ['Additional loan'])
# nb.show_note_by_id(2)
#Search Tests:
#nb.search_notes('memo')
#nb.search_notes('memo1')
#nb.search_notes('memo4')
#nb.search_notes('tag1')
#nb.search_notes('tag4')
#notes = nb.search_notes('tag') # This is a list, so to find substring, we need to search each term inside the list
#nb.show_notes(notes)

#Search the note by ID



