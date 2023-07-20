import controller, view

def begin_of_work():
    controller.main_menu()

def print_file():
    for i in controller.phonebook:
        print(i)

def open_book():
    with open(controller.path, 'r', encoding='UTF_8') as file:
        contacts = file.read().split('\n')
        controller.phonebook = contacts

def save_in_contacts():
    with open(controller.path, 'w', encoding='UTF_8') as file:
        file.write('\n'.join(controller.phonebook))

def add_new_contact():
    view.separator()
    open_book()
    print_file()
    view.separator()
    id_cont = int(input('Введите id для нового контакта: '))
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    contact = f'{id_cont}; {name}; {surname}; {patronymic}; {phone}; {comment}'
    controller.phonebook.append(contact)
    print_file()

def change_in_contacts():
    view.separator()
    open_book()
    print_file()
    view.separator()
    answer_id = int(input('Введите id контакта, который хотите изменить: '))
    contact = controller.phonebook.pop(answer_id).split('; ')
    print(contact)
    print('Выберите, что хотите поменять: \n '
        '1 - имя, 2 - фамилия, 3 - отчество, '
        '4 - номер телефона, 5 -комментарий ?')
    answer = int(input('Ваш выбор: '))
    contact[answer] = input('Введите новое значение: ')
    print(contact)
    controller.phonebook.insert(answer, ';'.join(contact))

def delete_from_contacts():
    view.separator()
    open_book()
    print_file()
    view.separator()
    answer_id = int(input('Введите id контакта для удаления: '))
    controller.phone_book.pop(answer_id)
    print_file()

def search_in_contacts():
    open_book()
    answer = int(input('Введите id контакта, который хотите найти: '))
    contact = controller.phone_book.pop(answer)
    print(contact)
    print('\n')  