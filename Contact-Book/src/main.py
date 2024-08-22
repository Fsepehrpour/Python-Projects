from collections import defaultdict

class ContactBook:
    def __init__(self):
        self.contacts = defaultdict(dict)

    def add(self, name, phone, email=None, address=None):
        if name in self.contacts:
            print('Contact already exists.')
            return # ???
        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email
        self.contacts[name]['address'] = address
        print('Contact added.')


    def view(self):
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-" * 50)

    def update(self, name, phone=None, email=None, address=None):
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
        if name not in self.contacts:
            print('Contact not found')
            return
        del self.contacts[name]
        print('Contact removed.')

if __name__ == "__main__":
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

