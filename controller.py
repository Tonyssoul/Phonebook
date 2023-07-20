import model, view

phonebook = []
path = 'PhoneBook.txt'

def start_menu():
    view.hi()
    while True:
        view.menu()
        answer = int(input('Выберите действие: '))
        if answer == 1:
            view.separator()
            model.open_book()
            model.print_file()
            view.separator()
        elif answer == 2:
            model.save_in_contacts()
            view.done()
        elif answer == 3:
            model.add_new_contact()
            view.done()
        elif answer == 4:
            model.change_in_contacts()
            view.done()
        elif answer == 5:
            model.delete_from_contacts()
            view.done()
        elif answer == 6:
            model.search_in_contacts()
            view.done()
        else:
            print('Конец программы')
            break