import model


def start_menu():
    while True:
        print('Главное меню:\n'
            '1. Открыть файл с контактами \n'
            '2. Записать файл с контактами \n'
            '3. Добавить контакт \n'
            '4. Изменить контакт \n'
            '5. Удалить контакт \n'
            '6. Поиск по контактам \n'
            '0. Выход из программы \n')
        answer = int(input('Выберите действие: '))
        if answer == 1:
            print('**********************************************')
            model.open_book()
            model.print_file()
            print('**********************************************')
        elif answer == 2:
            model.save_in_contacts()
            print('Файл успешно сохранен \n')
        elif answer == 3:
            model.add_new_contact()
            print('Контакт успешно добавлен \n')
        elif answer == 4:
            model.change_in_contacts()
            print('Контакт изменен')
        elif answer == 5:
            model.delete_from_contacts()
            print('Контакт удален')
        elif answer == 6:
            model.search_in_contacts()
            print('Контакт который вы искали')
        else:
            print('Конец программы')
            break