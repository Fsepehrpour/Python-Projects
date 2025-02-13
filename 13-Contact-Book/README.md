<img src="images/banner.png" width="200" height="250">

# Contact Book Application

## Overview
The Contact Book Application is a simple command-line program that allows users to manage a contact list. The application supports basic CRUD operations—Create, Read, Update, and Delete—enabling users to add, view, update, and delete contact information efficiently.

## Features 
* **Add Contacts**: Store contact information including name, phone number, email, and address.
* **View Contacts**: Display the list of all contacts along with their details.
* **Update Contacts**: Modify existing contact information.
* **Delete Contacts**: Remove a contact from the list.
* **User-friendly Interface**: Simple command-line interface for easy navigation and use.

## How to Use
1. **Run the Application**: Start the program by executing the script.
2. **Main Menu**:
    * **View Contacts**: Select option 1 to see all saved contacts.
    * **Add Contac**: Select option 2 to add a new contact. You will be prompted to enter your     name, phone number, email, and address.
    * **Update Contact**: Select option 3 to update an existing contact. You can change the phone number, email, and/or address.
    * **Delete Contact**: Select option 4 to delete a contact by name.
    * **Quit**: Select option 5 to exit the application.

```
--- Contact Book Application ---
1. View Contacts.
2. Add Contact.
3. Update Contact.
4. Delete Contact.
5. Quit.

Please choose an option: 2

Enter contact name: Jane Doe
Enter contact's phone number: 123-456-7890
Enter contact's email address: jane.doe@example.com
Enter contact's address: 123 Main St, Anytown, USA
Contact added.
```

## Requirements
Python 3.x

## Running the Program
* Ensure Python is installed on your system.
* Copy the script to a .py file.
* Open a terminal and navigate to the directory containing the file.
* Run the script using the command: `python filename.py`.


## Notes
* Duplicate contacts (by name) are not allowed.
* Fields other than the name are optional and can be left blank.
* The application will prompt and display messages to guide you through the operations.

## License
This project is open-source and available for personal or educational use.
