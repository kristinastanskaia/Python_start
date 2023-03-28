# Задача 2.
# Реализовать метакласс, позволяющий создавать всегда один
# и тот же объект класса.

class DocMeta(type):
    a = None

    def __call__(self):
        if self.a is None:
            a = type.__call__(self)
        return self.a


class MyClass(metaclass=DocMeta):
    pass


obj_1 = MyClass()
obj_2 = MyClass()

print(obj_1 is obj_2)
