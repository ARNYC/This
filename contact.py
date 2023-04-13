next_id = 0
class Contact:
    
    def __init__ (self,name, email=''):
        self.name = name
        self.email = email
  
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def show_contact(self):
        print('Name:',self.name, 
              'Email:',self.email)

class Supplier(Contact):
    def order(self, product):
        print("Ordering", product, "from", self.get_name())

class Relative(Contact):
    def inquire_health(self,disease):
        print("Health Report", "cured of", disease)

c1 =  Contact('Arun Rao')
c1.show_contact()
s1 = Supplier('Mugdha Bapat')
s1.show_contact()
s1.order('Session on OOP')
r1 = Relative("xyz",'xyz@gmail.com')
r1.show_contact()
r1.inquire_health('toothache')




