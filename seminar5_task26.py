"""
 Напишите программу, которая на вход принимает два числа A и B,
 и возводит число А в целую степень B с помощью рекурсии.
*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""


def rec_degree(numb, degree):
    if degree == 1:
        return numb
    elif degree == 0:
        return 1
    return numb * rec_degree(numb, degree - 1)


my_numb = int(input("Введите число: "))
my_degree = int(input("Введите целую степень: "))
print("Результат возведения в степень равен:", rec_degree(my_numb, my_degree))
