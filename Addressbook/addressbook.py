from contactFolio import Contact, Address

class Addressbook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,name,email):
        new_contact = Contact(name,email)
        self.contacts.append(new_contact)

    def show_all_contacts(self):
        for contact in self.contacts:
            contact.show_contact()

    def set_contact_address(self,name,address):
        for contact in self.contacts:
            if contact.name == name:
                contact.set_address(address)

    def search_contact(self, s_term):
        records_found = False
        for contact in self.contacts:
            if (s_term in contact.name or 
                s_term in contact.email or
                s_term in contact.address.street):
                contact.show_contact()
                records_found = True
        if records_found == False:
            print (f'No Records with {s_term} found')



            
'''
a1 = Addressbook()
a1.add_contact('Arun','arun2@gmail.com')
#set address is done in three steps, through two separate classes. 
# Is that how it is done or is there a cleaner way?
add1 =Address ('25 park,Great k, NY','11021')
a1.set_contact_address('Arun', add1)
a1.add_contact('Dave','dav2@gmail.com')
#set address is done in three steps, through two separate classes. 
# Is that how it is done or is there a cleaner way?
add1 =Address ('156 North street, Charlotte,NC','28021')
a1.set_contact_address('Dave', add1)

a1.show_all_contacts()
a1.search_contact('Das')
a1.search_contact('Dave')
a1.search_contact('gmail')
a1.search_contact('street')
a1.search_contact('NY')
'''
