class Contact_List():
    def __init__(self):
        self.lst = []

    def add_contact(self, contact):
        self.lst.append(contact)

    def display_list(self):
        for contact in self.lst:
            print(f'Name: {contact.name}\nEmail: {contact.email}\nTelephone: {contact.telephone}\n')