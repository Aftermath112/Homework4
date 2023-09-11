def input_error(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error! User with entered name doesn't exist. Please check the name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Error! Enter user name and phone correctly."

    return inner_func


@input_error
def hello_handler():
    return "How can I help you?"


contacts = {}


@input_error
def add_handler(name, phone):
    if name not in contacts:
        contacts[name] = int(phone)
    else:
        raise ValueError


@input_error
def change_handler(name, phone):
    if name in contacts:
        contacts[name] = int(phone)
    else:
        raise KeyError


@input_error
def phone_handler(name):
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


@input_error
def show_all_handler():
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def main():
    while True:
        cmd = input("Enter command ").lower()

        if cmd == "hello":
            print(hello_handler())
        elif cmd.startswith("add"):
            parts = cmd.split(" ")
            if len(parts) == 3:
                name, phone = parts[1], parts[2]
                result = add_handler(name, phone)
                if result is not None:
                    print(result)
            else:
                print("Give me name and phone please")
        elif cmd.startswith("change"):
            parts = cmd.split(" ")
            if len(parts) == 3:
                name, phone = parts[1], parts[2]
                result = change_handler(name, phone)
                if result is not None:
                    print(result)
            else:
                print("Give me name and phone please")
        elif cmd.startswith("phone"):
            parts = cmd.split(" ")
            if len(parts) == 2:
                name = parts[1]
                print(phone_handler(name))
            else:
                print("Command format is 'phone name' ")
        elif cmd.startswith("show all"):
            print(show_all_handler())
        elif cmd in ("good bye", "exit", "close"):
            print("Good bye!")
            break
        elif cmd in ("."):
            break
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
