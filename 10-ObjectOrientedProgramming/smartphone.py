from contact import Contact
from contact_list import Contact_List

if __name__ == '__main__':
    cl = Contact_List()
    cl.add_contact(Contact('John Brown', 'brown@onet.pl', '555234000'))
    cl.add_contact(Contact('Anna May', 'am@o2.pl', '232000199'))
    cl.add_contact(Contact('George Small', 'smallg@google.pl', '222999100'))
    cl.add_contact(Contact('Paola Big', 'bigpaola@poczta.pl', '100200300'))
    cl.display_list()
