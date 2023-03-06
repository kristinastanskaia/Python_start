"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
с повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
 Затем пользователь вводит сами элементы множеств.
"""
n = int(input("Cколько элементов в 1 списке?: "))
m = int(input("Cколько элементов во 2 списке?: "))
set_1 = [int(input("Вводите элемент 1го списка: ")) for i in range(n)]
print(*set_1, sep=', ')
set_1 = set(set_1)
set_2 = [int(input("Вводите элемент 2го списка: ")) for i in range(m)]
print(*set_2, sep=', ')
set_2 = set(set_2)
union = sorted(set_1.intersection(set_2))
print(*union, sep=', ')

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')