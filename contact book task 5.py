contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Contact added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    
    for idx, contact in enumerate(contacts):
        print(f"{idx + 1}. {contact['name']} - {contact['phone']}")
    print()

def search_contacts():
    search = input("Enter name or phone number to search: ")
    
    found_contacts = [contact for contact in contacts if search.lower() in contact['name'].lower() or search in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.\n")
        return
    
    for contact in found_contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}\n")

def update_contact():
    search = input("Enter name or phone number to update: ")
    
    found_contacts = [contact for contact in contacts if search.lower() in contact['name'].lower() or search in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.\n")
        return
    
    for contact in found_contacts:
        print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        name = input("Enter new name (leave blank to keep current): ")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        
        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        if address:
            contact['address'] = address
        print("Contact updated successfully.\n")

def delete_contact():
    search = input("Enter name or phone number to delete: ")
    
    global contacts
    contacts = [contact for contact in contacts if search.lower() not in contact['name'].lower() and search not in contact['phone']]
    
    print("Contact deleted successfully.\n")

def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
