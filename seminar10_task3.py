"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
start_list = ['attribute', 'класс', 'функция', 'type']
list_bytes = []
list_exception = []
for i in start_list:
    if i.isascii():
        list_bytes.append(bytes(i, "UTF-8"))
    else:
        list_exception.append(i)

print(list_bytes)
print(f"Невозможно записать в байтовом типе с помощью маркировки b'':"
      f" {list_exception}")
