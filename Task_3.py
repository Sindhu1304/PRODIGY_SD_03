import json
import os

# Define the path for the contacts file
contacts_file = 'contacts.json'

# Function to load contacts from the file
def load_contacts():
    if not os.path.exists(contacts_file):
        return {}
    with open(contacts_file, 'r') as file:
        return json.load(file)

# Function to save contacts to the file
def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

# Function to edit a contact
def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Main function to handle the contact management system
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()

