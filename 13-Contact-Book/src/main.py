from collections import defaultdict

class ContactBook:
    """
    A simple Contact Book application that allows users to add, view, update,
    and delete contacts. Each contact can have a name, phone number, email address,
    and physical address.
    """
    
    def __init__(self):
         """
        Initialize contact book object with an empty dictionary.
        """
        self.contacts = defaultdict(dict)

    def add(self, name, phone, email=None, address=None):
        """
        Adds a new contact to the contact book.

        :param str name: The name of the contact
        :param str phone: The phone number of the contact
        :param str email: The email address of the contact (optional)
        :param str address: The physical address of the contact (optional)
        """
        if name in self.contacts:
            print('Contact already exists.')
            return
        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email
        self.contacts[name]['address'] = address
        print('Contact added.')

    def view(self):
        """
        Displays all contacts in the contact book along with their details.
        """
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-" * 50)

    def update(self, name, phone=None, email=None, address=None):
        """
        Updates the information of an existing contact.

        :param str name: The name of the contact to update
        :param str phone: The new phone number of the contact (optional)
        :param str email: The new email address of the contact (optional)
        :param str address: The new physical address of the contact (optional)
        """
        if name not in self.contacts:
            print('Contact not found!')
            return

        if phone:
            self.contacts[name]['phone'] = phone

        if email:
            self.contacts[name]['email'] = email
        if address:
            self.contacts[name]['address'] = address
        print('Contact updated')

    def delete(self, name):
        """
        Deletes a contact from the contact book.

        :param str name: The name of the contact to delete
        """
        if name not in self.contacts:
            print('Contact not found')
            return
        del self.contacts[name]
        print('Contact removed.')

if __name__ == "__main__":
    """
    Main loop for the Contact Book application. 
    Provides a menu for the user to view, add, update, or delete contacts.
    """
    book = ContactBook()

    while True:
        print("\n--- Contact Book Application ---")
        print("1. View Contacts.")
        print("2. Add Contact.")
        print("3. Update Contact.")
        print("4. Delete Contact.")
        print("5. Quit.")
        user_choice = input('\nPlease choose an option.')

        if user_choice == '5':
            print('App is terminated!')
            break

        elif user_choice == '1':
            print('\nList of Contacs:')
            book.view()

        elif user_choice == '2':
            name = input("\nEnter contact name:")
            phone = input("\nEnter contact's phone number:")
            email = input("\nEnter contact's email addrees:")
            address = input("\nEnter contact's address:")
            book.add(name, phone, email, address)

        elif user_choice == '3':
            name = input("\nEnter name of the contact to update:")
            phone = input("\nEnter contact's new phone number:")
            email = input("\nEnter contact's new email addrees:")
            address = input("\nEnter contact's new address:")
            book.update(name, phone or None, email or None, address or None)

        elif user_choice == '4':
            name = input(input("\nEnter contact name to delete:"))
            book.delete(name)

        else:
            print("\nInvalid choice! Please try again:")

