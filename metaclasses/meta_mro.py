out = []

class Meta(type):
    def __init__(cls, name, bases, ns):
        if name == 'C':
            def foo(self):
                out.append("C.foo (injected)")
                return super(cls, self).foo()
            cls.foo = foo
        super().__init__(name, bases, ns)

class A(metaclass=Meta):
    def foo(self):
        out.append("A.foo")

class B(A, metaclass=Meta):
    def foo(self):
        out.append("B.foo");
        return super().foo()

class C(B, A, metaclass=Meta):
    pass

C().foo()
print(out)
