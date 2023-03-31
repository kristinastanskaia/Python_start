"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.
*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!
Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""
start_list = ['разработка', 'сокет', 'декоратор']
list_1 = []
for i in start_list:
    a = str(i.encode('unicode_escape'))
    list_1.append(a)
    print(
        f"'{i}' - слово в буквенном формате, тип переменной: {type(i)}, "
        f"содержимое: {i}, длина: {len(i)}")
    print()
    print(
        f"{a} - слово в формате кодовых точек Unicode, тип переменной: "
        f"{type(a)}, содержимое: {a}, длина: {len(a)}")
    print()
