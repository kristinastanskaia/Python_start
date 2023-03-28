# Задача 1.
# Реализовать дескрипторы для любых двух классов.


class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным!")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class PayRoll:
    rate = NonNegative()  # кол-во смен
    working_shift = NonNegative()  # ставка за смену

    def __init__(self, rate, working_shift):
        self.rate = rate
        self.working_shift = working_shift

    def total_profit(self):
        return self.rate * self.working_shift


class StringVerification:

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError('Аргумент может быть только строкой!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Person:
    surname = StringVerification()
    job_title = StringVerification()

    def __init__(self, surname, job_title):
        self.surname = surname
        self.job_title = job_title

    def get_name(self, surname, job_title):
        print(f'Сотрудник: {surname}, должность: {job_title} ')


# проверка 1
OBJ = PayRoll(10, 4000)
print(f"Зарплата равна: {OBJ.total_profit()}")

# проверка 2
OBJ.rate = 30
OBJ.working_shift = 2000
salary = OBJ.total_profit()
print(f"Зарплата равна: {salary}")

employee = Person(surname='', job_title='')
employee.surname = "Станская"
employee.job_title = "тестировщик"
employee.get_name(employee.surname, employee.job_title)
