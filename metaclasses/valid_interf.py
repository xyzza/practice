class RequiresCM(type):
    def __init__(cls, name, bases, ns):
        if name != 'Base' and not all(m in cls.__dict__ for m in ('__enter__','__exit__')):
            raise TypeError(f"{name} must define __enter__ and __exit__")
        super().__init__(name, bases, ns)

class Base(metaclass=RequiresCM): pass

class Bad(Base):
    def __enter__(self): pass
