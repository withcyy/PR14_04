class check_attribute(type):
    attributes = ['attr1', 'attr2']

    def __new__(cls, name, bases, dct):
        for attr in cls.attributes:
            if attr not in dct:
                raise AttributeError(f"in class {name} no attr {attr}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=check_attribute):
    attr1 = "one"
    attr2 = "two"

try:
    class MyOtherClass(metaclass=check_attribute):
        attr1 = "one"
except AttributeError as e:
    print(e)  