"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml


def yaml_save_data():
    my_data = {
        1: ['kristi', 'anton', 'karl'],
        2: 4477,
        3: {1: '\u04E0', 2: '\u14DF', 3: '\u0A07'}
    }

    with open('File.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(my_data, yaml_file, default_flow_style=False,
                  allow_unicode=True)


def read_yaml_file():
    try:
        with open('File.yaml', 'r', encoding='utf-8') as read_file:
            content = yaml.Loader(read_file)
            return content
    except FileNotFoundError:
        print('файла не существует')


yaml_save_data()
print(read_yaml_file())
