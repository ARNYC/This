# Note
# id, create_on, memo, tags (list of strings)
import datetime
last_id = 0
'''
Functionality:
create
modify: memo, tags
search
show
getter: id
'''
class Note:
    # TODO: Add code for assigning today's date
    def __init__(self, memo, tags=[]):
        global last_id
        last_id = last_id + 1
        self.id = last_id
        self.created_on = datetime.date.today()
        self.memo = memo
        self.tags = tags

    def modify_memo(self, memo):
        self.memo = memo
        
    def add_tags(self,tags=[]):
        print("self_tags, tags-type",type(self.tags), type(tags))
        self.tags.extend(tags)

    # given a search term, search memo and tags, see if it contains the search term. If it does,
    # return for the moment "true " or else false. Later may be it will return the note number

    def search_note(self,s_term):
        #if s_term in self.memo or s_term in self.tags:
        for tag in self.tags:
            if s_term in tag:
                return True
        if s_term in self.memo :
            return True 
        return False
    
    def get_id(self):
        return self.id
    
    def show_note(self):
        print("Id:",self.id, "Created on:",self.created_on,"Memo:", self.memo,"Tags:", self.tags)
        #print("Memo:", self.memo)
        #print("Tags:", self.tags)

'''
n1 = Note("Year end preps")
n1.show_note()

n2 = Note("Auditing work")
print(n2.id, n2.created_on, n2.memo, n2.tags)

n3 = Note("Loan reclamation", ["loan", "yearly"])
n3.show_note()

n3.modify_memo("Mortage Loan reclamation")
print(n3.id, n3.created_on, n3.memo, n3.tags)

n3.add_tags(["secured", "balloon"])
print(n3.id, n3.created_on, n3.memo, n3.tags)

n3 = Note("Loan reclamation", ["loan", "yearly"])
n3.show_note()
n3.add_tags(["secured", "balloon"])
print(n3.id, n3.created_on, n3.memo, n3.tags)
print(n3.search_note('ball'))
'''