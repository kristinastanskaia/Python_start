"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
start_list = ['class', 'function', 'method']
list_1 = []
for i in start_list:
    list_1.append(bytes(i, "UTF-8"))
for i in list_1:
    print(f'Слово в байтовом формате: {i}')
    # for bytes in i:
    #   print(bytes, end=' ')
    print(f'Тип переменной: {type(i)}')
    print(f'Содержимое переменной: {(str(i, "UTF-8"))}')
    print(f'Длина переменной: {len(i)}')
    print()
