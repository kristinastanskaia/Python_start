"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
 str
str(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


class Worker:
    def __int__(self, *args):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def get_full_name(self, name, surname, position):
        print(f'Сотрудник: {name} {surname}, должность: {position} ')

    def get_total_income(self, wage, bonus):
        print(f'Зарплата сотрудника: {wage + bonus}')


worker = Position()
worker.get_full_name('Кристина', 'Станская', 'тестировщик')
worker.get_total_income(150000, 50000)
