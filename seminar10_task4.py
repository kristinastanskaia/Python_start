"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
start_list = ['разработка', 'администрирование', 'protocol', 'standard']
list_encode = []
list_decode = []
for i in start_list:
    list_encode.append(i.encode('utf-8'))
print(f"В байтовом представлении:  {list_encode}")

for i in list_encode:
    list_decode.append(i.decode('utf-8'))
print(f"В строковом представлении: {list_decode}")
