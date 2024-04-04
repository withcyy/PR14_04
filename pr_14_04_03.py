class ForbiddenInheritanceMeta(type):
    def __new__(cls, name, bases, dct):
        forbidden_classes = (ForbiddenClass1, ForbiddenClass2)

        for forbidden_class in forbidden_classes:
            if any(issubclass(base, forbidden_class) for base in bases):
                raise TypeError(f"Class '{name}' cannot inherit from '{forbidden_class.__name__}'")

        bases = tuple(reversed(bases))

        return super().__new__(cls, name, bases, dct)

class ForbiddenClass1:
    pass

class ForbiddenClass2:
    pass

class MyClass(metaclass=ForbiddenInheritanceMeta):
    pass

try:
    class MySubclass1(MyClass, ForbiddenClass1):
        pass
except TypeError as e:
    print(e)

try:
    class MySubclass2(ForbiddenClass2, MyClass):
        pass
except TypeError as e:
    print(e)
