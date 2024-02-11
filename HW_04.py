def parse_input(user_input: str): # Парсинг введених даних
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):    # Декоратор для функцій
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "The data is not entered correctly"          
    return inner

@input_error                                           
def add_contact(args: str, contacts: dict): # Функія додавання контактів
    name, phone = args      
    if name in contacts:
        return f'Контакт {name} вже існує.'
    else:
        contacts[name] = int(phone)        
        return f'Контакт {name} додано.'
             
@input_error   
def change_contact(args: str, contacts: dict): # Функія заміни контактів
    name, phone = args 
    contacts[name] == name        
    contacts[name] = phone  
    return f'Контакт {name} змінено.'      

@input_error    
def del_contact(args: str, contacts: dict ): # Функія видалення контактів
        name, = args
        contacts.pop(name)
        return f"Контакт {name} видалено"        
   

def main():  # основна функція виклику
    contacts = {} 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        match command:
            case "close"|"exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "all":
                print(contacts)
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "del":
                print(del_contact(args, contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()