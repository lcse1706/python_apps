def add_contact():
    try:
        first_name = input("Enter contact's first name: ")
        last_name = input("Enter contact's last name: ")
        phone = input("Enter contact's phone number: ")
        with open("contacts.txt", "a") as file:
            file.write(f"{first_name} {last_name},{phone}\n")
        print("Contact added successfully!")
    except Exception as e:
        print(f"An error occurred while adding the contact: {e}")

def show_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.read().splitlines()
        if contacts:
            print("\nYour Contacts:")
            for i, contact in enumerate(contacts, start=1):
                name, phone = contact.split(",")
                print(f"{i}. {name} - {phone}")
        else:
            print("No contacts found.")
    except FileNotFoundError:
        print("No contacts found. Add a contact first.")

def search_contact():
    try:
        query = input("Enter first or last name to search: ").lower()
        with open("contacts.txt", "r") as file:
            contacts = file.read().splitlines()
        found_contacts = [c for c in contacts if query in c.split(",")[0].lower()]
        if found_contacts:
            print("\nSearch Results:")
            for i, contact in enumerate(found_contacts, start=1):
                name, phone = contact.split(",")
                print(f"{i}. {name} - {phone}")
        else:
            print("No matching contacts found.")
    except FileNotFoundError:
        print("No contacts found. Add a contact first.")

def delete_contact():
    try:
        query = input("Enter full name (first and last name) to delete: ").lower()
        with open("contacts.txt", "r") as file:
            contacts = file.read().splitlines()
        
        updated_contacts = [c for c in contacts if query != c.split(",")[0].lower()]

        if len(updated_contacts) < len(contacts):
            with open("contacts.txt", "w") as file:
                for contact in updated_contacts:
                    file.write(contact + "\n")
            print("Contact deleted successfully!")
        else:
            print("No matching contact found to delete.")
    except FileNotFoundError:
        print("No contacts found. Add a contact first.")

  
  
def main():
  while True:
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
    
    try:
      choice = int(input("Please choose an option: "))
      print("\n")
    except ValueError:
      print("Invalid choice. Please choose between 1-5.")
      continue
    
    match choice:
      case 1:
        add_contact()
      case 2: 
        show_contacts()
      case 3:
        search_contact()
      case 4:
        delete_contact()
      case 5:
        print("Exiting Contact Book. Bye !")
        break
      case _:
        print("Invalid option, try again !\n")


if __name__ == "__main__":
  main()