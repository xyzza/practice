class RegistryMeta(type):
    registry = None

    def __new__(mcls, name, bases, ns):
        if mcls.registry is None:
            mcls.registry = []
        return super().__new__(mcls, name, bases, ns)

    def __init__(cls, name, bases, ns):
        if name != 'Base':
            cls.registry.append(name)
        super().__init__(name, bases, ns)

class MyReg(RegistryMeta):
    # registry = []
    pass

class Base(metaclass=RegistryMeta): pass
class A(Base): pass
class B(Base): pass

print(RegistryMeta.registry)
print(MyReg.registry)
