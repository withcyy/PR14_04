class add_func_meta(type):
    def __new__(cls, name, bases, dct):
        dct['add_func'] = lambda self: print("added func")
        return super().__new__(cls, name, bases, dct)

class my_class(metaclass=add_func_meta):
    def __init__(self, value):
        self.value = value

obj = my_class(123)
obj.add_func()