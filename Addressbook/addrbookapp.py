import sys, os
from addressbook import Addressbook
from contactFolio import Address

class Addr_book_app:
    def __init__(self):
        self.addressbook = Addressbook()
        self.choices = {
             1: self.add_contact,
             2: self.set_contact_address,
             3: self.modify_contact,
             4: self.show_contact,
             5: self.search_contact,
             6: self.quit
        }

    def run(self):
        while True:
            #os.system('cls')
            self.display_menu()
            selection = int(input ('Enter your choice: '))
            action = self.choices[selection]
            if action:
                 os.system('cls')
                 action()
            else:
                 print('enter a valid choice')

    def display_menu(self):
            print('Address book Menu')
            print('1. add contact')
            print('2. add address to contact')
            print('3. modify contact')
            print('4. show contact')
            print('5. search for a contact')
            print('6. quit')

    def add_contact(self):
         name = input('Add Contact: Enter contact name: ')
         email = input('            Enter contact email: ')
         street = input('            Enter Street Address: ')
         zip_code = input('            Enter Zip Code: ')    
         address = Address(street,zip_code)
         self.addressbook.add_contact(name,email)
         self.addressbook.set_contact_address(name,address)

    def set_contact_address(self):
         pass
    
    def modify_contact(self):
        pass

    def show_contact(self):
        self.addressbook.show_all_contacts()

    def search_contact(self):
        pass

    def quit(self):
         sys.exit(0) 


if __name__ == "__main__":
    Addr_book_app().run()


        
        
        