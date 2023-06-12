# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных


import csv

# функция для вывода данных из справочника
def display_contacts():
    with open('contacts.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(row)

# функция для сохранения данных в текстовом файле
def save_contacts(name, phone):
    with open('contacts.txt', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])

# функция для поиска определенной записи по имени или фамилии
def search_contacts(search_term):
    with open('contacts.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if search_term in row:
                print(row)

# функция для изменения данных в справочнике
def edit_contact(old_name, new_name, new_phone):
    rows = []
    with open('contacts.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == old_name:
                row[0], row[1] = new_name, new_phone
            rows.append(row)

    with open('contacts.txt', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# функция для удаления записи из справочника
def delete_contact(name):
    rows = []
    with open('contacts.txt', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] != name:
                rows.append(row)

    with open('contacts.txt', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# основной цикл программы
while True:
    print("1. Просмотреть контакты")
    print("2. Добавить контакт")
    print("3. Поиск контакта")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        display_contacts()
    elif choice == '2':
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        save_contacts(name, phone)
    elif choice == '3':
        search_term = input("Введите имя или фамилию: ")
        search_contacts(search_term)
    elif choice == '4':
        old_name = input("Введите имя контакта: ")
        new_name = input("Введите новое имя контакта: ")
        new_phone = input("Введите новый номер телефона: ")
        edit_contact(old_name, new_name, new_phone)
    elif choice == '5':
        name = input("Введите имя контакта: ")
        delete_contact(name)
    elif choice == '6':
        break
    else:
        print("Неверный выбор")