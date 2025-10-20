import re
import os

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def validate_phone_number(phone_number:str)->str:
    rеt_phone_number = re.sub(r'[^0-9+]', '', phone_number)

    if len(rеt_phone_number) < 12 or len(rеt_phone_number)>13:
        return ""

    if len(rеt_phone_number) == 12:
        if rеt_phone_number[0] == "+":
            return ""
        else:
            rеt_phone_number = "+"+rеt_phone_number

    return rеt_phone_number

def add_contact(args:[], contacts:{})->str:
    if len(args) < 2:
        return "Inavlid data arguments!"
    
    name = args[0]
    args.remove(name) 
    phone = "".join(args) #for support phone format with spaces +38 (097) xxx xx xx

    phone = validate_phone_number(phone)
    if len(phone) == 0:
        return "Inavlid phone number! Enter the phone number in the format: +xx (xxx) xxx xx xx"
    
    name = name.capitalize()
    contacts[name] = phone
    return "Contact added."

def change_contact(args:[], contacts:{})->str:
    if len(args) < 2:
        return "Inavlid data arguments!"
    name = args[0]

    args.remove(name) 
    phone = "".join(args) #for support phone format with spaces +38 (097) xxx xx xx

    phone = validate_phone_number(phone)
    if len(phone) == 0:
        return "Inavlid phone number! Enter the phone number in the format: +xx (xxx) xxx xx xx"
    
    name = name.capitalize()
    contacts[name] = phone
    return "Contact changed."

def get_phone_by_name(args:[], contacts:{})->str:
    name = args[0] if len(args)>0 else None
    if name is None:
        return "Invalid name!"
    
    name = name.capitalize()
    if contacts.get(name) is None:
        return "Record is missing!"
    
    return contacts.get(name)

def safe_add_contact(args:[], contacts:{})->str:
    if len(args)>0 and contacts.get(args[0].capitalize()) is not None:
        print("This contact already exists. Do you want to update it (enter 'y' to confirm)?")
        if parse_input(input())[0] == "y":
            return change_contact(args,contacts)
        else:
            return"Command ignored."
        
    return add_contact(args, contacts)

def safe_change_contact(args:[], contacts:{})->str:
    if len(args)>0 and contacts.get(args[0].capitalize()) is None:
        print("This contact is missing. Would you like to add new acc (enter 'y' to confirm)?")
        if parse_input(input())[0] == "y":
            return add_contact(args,contacts)
        else:
            return "Command ignored."  
        
    return change_contact(args, contacts)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(safe_add_contact(args,contacts))
        elif command == "change":
            print(safe_change_contact(args,contacts))
        elif command == "phone":
            print(get_phone_by_name(args,contacts))
        elif command == "all":
            print(contacts)
        elif command == "clear":
            clear_console()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()