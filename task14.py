"""
Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N.
"""
total = int(input("Введите число N: "))
i = 0
num = 2
while True:
    if num ** i <= total:
        print(num ** i)
        i += 1
    else:
        break