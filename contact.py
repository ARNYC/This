next_id = 0
class Contact:
    
    def __init__ (self,first_name, last_name):
        self.contact_id = next_id+1
        self.first_name = first_name
        self.last_name = last_name
        #self.address = ''
        #self.city =''
        #self.zip_code =''
        self.company = ''
        self.phone_no = []
        #self.email_id = ''
        #question: I want to discuss briefly the big picture.Company will
        # have its own address. etc. How do you plan classes? how do you link them?
        #do you have a class for each table in database?

        #question 2: Doesn't the class always get influenced by how the GUI
        # id designed?  Is it not easier to design a screen with all attributes
        # and all get passed with the click of a button (with empty cells passing 
        # default value of None)?

    
    def get_last_name(self):
        return self.last_name
    
    def get_phone_no(self):
        return self.phone_no
    
    def show_contact(self):
        print('id:',self.contact_id, 'First Name:',self.first_name, 
              'last name:',self.last_name, 'Company:',self.company,
              'Phone no:',self.phone_no)
        #Question: is it good to have print statement here or 
        #          should it return the values as a list?

    def search_by_phone_no(self,phone_no):

        for num in self.phone_no:
            if num == phone_no:
                return True
        return False
    
    def search_by_last_name(self,last_name):
        if self.last_name == last_name:
            return True
        else:
            return False
    
    def modify_contact(self,first_name,last_name,phone_no):
        pass

c1 =  Contact('Arun','Rao')
c1.company = 'GCG'
c1.phone_no =['3475551212', '3479683657'] 
#c1.show_contact()
print(c1.get_phone_no())
print(c1.search_by_phone_no('3479683657'))
print(c1.search_by_phone_no('3471113657'))
print(c1.search_by_last_name('Rao'))
print(c1.search_by_last_name('Rai'))



