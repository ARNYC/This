next_id = 0
class Contact:
    
    def __init__ (self,name,email=''):
       # self.contact_id = 'c'+str(next_id+1)
        self.name = name
        self.address = Address(street=None, zip_code=None)
        self.email = email

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_address(self):
        return self. address
    
    def set_address(self,address):
        self.address = address

    
    def show_contact(self):
        print('Name:',self.name,'\n',
              'Address:',self.address.street,'\n','Email:',self.email)


    def search_by_email(self,email):

        for num in self.email:
            if num == email:
                return True
        return False
    
    def search_by_name(self,name):
        if self.name == name:
            return True
        else:
            return False
    
    def modify_contact(self,name = '',email = ''):
        if name:
            self.name = name 
        if email :
            self.email = email
            


class Address:
    def __init__ (self,street,zip_code):
        self.street = street
        self.zip_code = zip_code

    def show_address(self):
        print(self.street, self.zip_code)
    
    def modify_address(self, new_street ='',new_zip_code =''):
        if new_street:
            self.street = new_street
        if new_zip_code:
            self.zip_code = new_zip_code


'''
c1 =  Contact('Arun Rao','arun@gmail.com')
c2 = Contact('xyz','xyz@gmail.com')
#c1.email =['3475551212', '3479683657'] 
#c1.show_contact()
print(c1.get_email())
print(c1.search_by_email('3479683657'))
print(c1.search_by_email('3471113657'))
print(c1.search_by_name('Arun Rao'))
ca1 = Address('25 Park Place,Great Neck,NY','11021')
ca1.show_address()
c1.set_address(ca1)
c1.show_contact()
ca2 = Address('k Ptrtr,y5555 hk,NY,hh21','10001')
ca2.show_address()
c2.set_address(ca2)
c2.show_contact()
c1. modify_contact('Chaitali Das')
c1.show_contact()
#modify address is done in three steps, through two separate classes. 
# Is that how it is done or is there a cleaner way?
ca2.modify_address('25 luxur street')
c2.set_address(ca2)
c2.show_contact()'''

