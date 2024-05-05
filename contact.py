class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, search_term, updated_contact):
        for i, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                self.contacts[i] = updated_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, search_term):
        for i, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            search_term = input("Enter name or phone number to update: ")
            new_name = input("Enter new name: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            updated_contact = Contact(new_name, new_phone_number, new_email, new_address)
            contact_book.update_contact(search_term, updated_contact)
        elif choice == "5":
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
