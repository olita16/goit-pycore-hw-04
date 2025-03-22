def parse_input(user_input):
    user_input = user_input.strip()
    if not user_input:
        return None, None 
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def validate_args(command, args):
    command_usage = {
        "add": "Usage: add [name] [phone number]",
        "change": "Usage: change [name] [phone number]",
        "phone": "Usage: phone [name]",
        "all": "Usage: all"
    }
    
    if command in command_usage:
        if command == "all" and args:
            return False, command_usage["all"]
        elif command == "phone" and len(args) != 1:
            return False, command_usage["phone"]
        elif len(args) != 2 and command in ["add", "change"]:
            return False, command_usage[command]
    return True, ""

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args, contacts):
    name = args[0]
    return f"{name}'s phone number: {contacts.get(name, 'Contact not found.')}"

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {} 
    print("Welcome to the assistant bot!")
    
    commands = {
        "hello": lambda: print("How can I help you?"),
        "add": lambda args: print(add_contact(args, contacts)),
        "change": lambda args: print(change_contact(args, contacts)),
        "phone": lambda args: print(show_phone(args, contacts)),
        "all": lambda _: print(show_all(contacts)),
    }

    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command is None:
            print("Invalid command.")
            continue

        is_valid, error_message = validate_args(command, args)
        if not is_valid:
            print(error_message)
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command in commands:
            commands[command](args)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
