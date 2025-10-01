import os

FILENAME = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    with open(FILENAME, "a") as f:
        f.write(f"{name},{phone},{email}\n")
    print("Contact added.\n")

def view_contacts():
    print("\nAll Contacts:")
    try:
        with open(FILENAME, "r") as f:
            contacts = f.readlines()
            if not contacts:
                print("No contacts found.")
                return
            print("{:<20} {:<15} {:<30}".format("Name", "Phone", "Email"))
            print("-" * 65)
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"{name:<20} {phone:<15} {email:<30}")
    except FileNotFoundError:
        print("No contacts file found.\n")

def search_contact():
    keyword = input("Enter name to search: ").lower()
    found = False
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                if keyword in name.lower():
                    print(f"\nFound: {name}, {phone}, {email}")
                    found = True
        if not found:
            print("No matching contact found.")
    except FileNotFoundError:
        print("No contacts file found.\n")

def edit_contact():
    name_to_edit = input("Enter the name of the contact to edit: ").lower()
    updated = False
    lines = []

    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        with open(FILENAME, "w") as f:
            for line in lines:
                name, phone, email = line.strip().split(",")
                if name.lower() == name_to_edit:
                    print(f"Editing contact: {name}")
                    name = input("New name: ")
                    phone = input("New phone: ")
                    email = input("New email: ")
                    updated = True
                f.write(f"{name},{phone},{email}\n")

        if updated:
            print("Contact updated.\n")
        else:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts file found.\n")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ").lower()
    deleted = False
    lines = []

    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        with open(FILENAME, "w") as f:
            for line in lines:
                name, phone, email = line.strip().split(",")
                if name.lower() != name_to_delete:
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            print("Contact deleted.\n")
        else:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts file found.\n")

def main():
    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
