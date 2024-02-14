import pandas as pd
import csv


def control_func() -> None:
    """
    Управляющая функция, реализует выбор действий пользователя
    :return: None
    """
    while True:
        print("\nМеню для управления справочником. Выберите желаемое действие")
        user_val = input("1 - создать запись\n2 - изменить запись\n3 - найти запись\n"
                         "4 - вывести список записей в справочнике\n5 - выйти из программы\n")
        if user_val == '1':
            create_record()
        elif user_val == '2':
            change_record()
        elif user_val == '3':
            for i in seeker():
                print(i)
        elif user_val == '4':
            with open("data.csv", encoding="windows-1251") as reader_file:
                reader_data = csv.reader(reader_file, delimiter=";")
                for row in reader_data:
                    print(row)
        elif user_val == '5':
            break
        else:
            print("Вы ошиблись с выбором, попробуйте еще раз\n")


def create_record() -> None:
    """
    Функция реализует метод для добавления записей в справочник
    :return: None
    """
    simple_dict = []
    name = input("Введите Имя\n")
    second_name = input("Введите Фамилию\n")
    third_name = input("Введите Отчество\n")
    organization = input("Введите Организацию\n")
    work_phone = input("Введите Рабочий номер телефона\n")
    personal_phone = input("Введите Сотовый номер телефона\n")
    simple_dict.append([second_name, name, third_name, organization, work_phone, personal_phone])
    headers = ['second_name', 'name', 'third_name', 'organization', 'work_phone', 'personal_phone']
    pd.DataFrame(simple_dict, columns=headers). \
        to_csv('data.csv', mode='a', sep=';', encoding='windows-1251', header=False, index=False)
    # Создание новой записи при помощи модуля Pandas
    print("Новая запись создана!")


def change_record() -> None:
    """
    Функция реализует метод для изменения записи в справочнике
    :return: None
    """
    mid_list = []
    middle_val = seeker()   # Присваиваем переменной результат поиска записи
    print(f"Найдены следующие записи:\n{list(middle_val)}")
    if len(middle_val) > 1:
        print("Уточните ваш запрос")
        change_record()     # Выбор записи для изменения
    else:
        print("Создайте новую запись")
        create_record()     # Создание новой записи
        with open("data.csv", mode='r', encoding='windows-1251') as reader:     # Отсеиваем ненужную запись
            for row in reader.readlines():
                if ";".join(middle_val[0]) not in row:
                    mid_list.append(row)
        with open("data.csv", mode='w', encoding="windows-1251") as new_reader:     # Переписываем справочник
            for new_row in mid_list:
                new_reader.write(new_row)
        # pd.read_csv("data.csv", encoding='windows-1251').drop(x, axis=0)


def seeker() -> list:
    """
    Функция для поиска записей по запросу пользователя
    :return: list
    """
    rez_list = []
    seek_value = input("Введите значение для поиска\n")
    with open("data.csv", encoding="windows-1251") as reader_file:
        reader_data = csv.reader(reader_file, delimiter=";")
        for row in reader_data:
            if seek_value.capitalize() in row or seek_value in row:     # Отсев по заданному значению
                rez_list.append(row)     # Запись найденной записи в список
        if len(rez_list) == 0:
            print("Такой записи в справочнике нет")
        else:
            return rez_list


if __name__ == '__main__':
    control_func()
