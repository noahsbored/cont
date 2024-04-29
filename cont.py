import re

#alright, this was hard work. for the sake of honesty ill admit that i got chatgpt to generate the  regex pattern to verify the email, i refuse to write something that looks like someone had a stroke on there keyboard, even if it means sacrificing my grades. everything else was written by me and it took hours.

contacts = {}

def display_menu():
    
    print("menu:")
    print("1. add a new contact")
    print("2. edit a contact")
    print("3. delete a contact")
    print("4. search for a contact")
    print("5.  show contacts")
    print("6. export contacts to a text file")
    print("7. import contacts from a file")
    print("8. quit")

def add_contact():
    
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")

    #
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        print("invalid format make sure you spelled it right and that theres a @. and it cant be some weird ass format like @hotmail.com ")
        return

    contacts[email] = {"Name": name, "Phone": phone_number, "Email": email}
    

def edit_contact():
    email = input("enter email of the contact you want to edit ")
    if email in contacts:
        print (contacts[email])
        name = input("enter new name: ")
        phone_number = input("enter new number: ")
        contacts[email] = {"Name": name, "Phone": phone_number, "Email": email}
        print("done.")
    else:
        print("there was a problem, either the contact didint exist, or some other weird thing happened.")

def delete_contact():
    email = input("enter email  of the contact to delete: ")
    if email in contacts:
        del contacts[email]
        print("deleted.")
    else:
        print("contact not found.")

def search_contact():
    email = input("enter email of the contact to search: ")
    if email in contacts:
    
        print("Name:", contacts[email]["Name"])
        print("Phone number:", contacts[email]["Phone"])
        print("Email address:", contacts[email]["Email"])
    else:
        print("contact not found.")

def display_all_contacts():
    if contacts:
        print("All contacts:")
        for email, contact in contacts.items():
            print("Email:", email)
            print("Name:", contact["Name"])
            print("Phone number:", contact["Phone"])
            print()
    else:
        print("no contacts found.")

def export_contacts():
    filename = input("Enter the file name to export contacts to: ")
    with open(filename, "w") as file:
        for email, contact in contacts.items():
            file.write(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {email}\n")



def import_contacts():
    try:
        filename = input("Enter the file name to import from: ")
        with open(filename, "r") as file:
            for line in file:
                name_match = re.search(r'Name: (.*?),', line)
                phone_match = re.search(r'Phone: (.*?),', line)
                email_match = re.search(r'Email: (.*?)$', line)
                if name_match and phone_match and email_match:
                    name = name_match.group(1)
                    phone = phone_match.group(1)
                    email = email_match.group(1)
                    contacts[email] = {"Name": name, "Phone": phone, "Email": email}
                    print(f"Imported contact: Name: {name}, Phone: {phone}, Email: {email}")
           
        
    
        print("imported contacts:")
        for email, contact in contacts.items():
            print("Name:", contact["Name"])
            print("Phone number:", contact["Phone"])
            print("Email address:", contact["Email"])
            print()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


main()
