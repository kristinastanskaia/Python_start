"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import re
import csv


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    my_list = [
        r'Изготовитель системы:\s+([a-zA-Z]+)',
        r'Название ОС:\s+([a-zA-Z0-9А-Яа-я\s\.]{1,})[\n]',
        r'Код продукта:\s+([-0-9a-zA-Z]+)',
        r'Тип системы:\s+([-0-9a-zA-Z\s]+)[\n]',
    ]
    system_prod = []
    name = []
    prod_code = []
    system_type = []
    for i in files:
        with open(i, encoding='cp1251') as file_in:
            input_data = file_in.read()
        system_prod.append(','.join(re.findall(my_list[0], input_data)))
        name.append(','.join(re.findall(my_list[1], input_data)))
        prod_code.append(','.join(re.findall(my_list[2], input_data)))
        system_type.append(','.join(re.findall(my_list[3], input_data)))
    main_data = [['Изготовитель системы ', 'Название ОС ', 'Код продукта ',
                  'Тип системы '], [], [], []]
    for i in range(len(name)):
        main_data[i + 1].append(system_prod[i])
        main_data[i + 1].append(name[i])
        main_data[i + 1].append(prod_code[i])
        main_data[i + 1].append(system_type[i])
        return main_data


def write_csv(filename):
    with open("data_report.csv", 'w', encoding='cp1251') as f_t:
        csv_file = csv.writer(f_t, delimiter=',')
        data = get_data()
        for i in data:
            csv_file.writerow(i)


write_csv("data_report.csv")

with open('data_report.csv', encoding='cp1251') as file_in:
    data = file_in.read()
    print(data)
