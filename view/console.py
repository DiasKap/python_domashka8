from .text import *


def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)


def print_message(message: str):
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')


def show_contacts(book: list[dict[str, str]]):
    if book:
        print('\n' + '=' * 67)
        for contact in book:
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{uid:>3}. {name:<20} {phone:<20} {comment:<20}')
        print('=' * 67 + '\n')
    else:
        print(book_error)


def input_contact(message: str) -> dict[str, str]:
    print(message)
    name = input(new_contact[0])
    phone = input(new_contact[1])
    comment = input(new_contact[2])
    return {'name': name, 'phone': phone, 'comment': comment}


def input_return(message: str) -> str:
    return input(message)

def input_change_contact(name, new_number):
    with open('phones.txt', 'r') as f:
        lines = f.readlines()
    with open('phones.txt', 'w') as f:
        for line in lines:
            if line.startswith(name):
                f.write(f'{name}: {new_number}\n')
            else:
                f.write(line)

def delete_contact(name):
    with open("phones.txt", "r") as f:
        lines = f.readlines()
    with open("phones.txt", "w") as f:
        for line in lines:
            if name not in line:
                f.write(line)
    print(f"Kontakt  {name} gelöscht")