class registr_meta(type):
    registr = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)

        cls.registr[name] = new_class
        return new_class

class MyClass1(metaclass=registr_meta):
    pass

class MyClass2(metaclass=registr_meta):
    pass

print(registr_meta.registr)