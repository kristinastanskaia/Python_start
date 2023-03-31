"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86
3 5 32
2 4 6
-1 64 -8
3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                print("{:4d}".format(self.my_list[i][j]), end="")

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]

        return Matrix.__str__(self)


matrix_one = Matrix([[5, 3], [9, 2]])
matrix_two = Matrix([[1, 5], [4, 1]])

print(Matrix.__add__(matrix_one, matrix_two))
