out = []
# breakpoint()
class Meta(type):
    @classmethod
    def __prepare__(mcls, name, bases):
        # breakpoint()
        out.append("Meta.__prepare__"); return {}
    def __new__(mcls, name, bases, ns):
        # breakpoint()
        out.append("Meta.__new__"); return super().__new__(mcls, name, bases, ns)
    def __init__(cls, name, bases, ns):
        # breakpoint()
        out.append("Meta.__init__"); super().__init__(name, bases, ns)

class C(metaclass=Meta):
    # breakpoint()
    out.append("class body")
    def __new__(cls):
        # breakpoint()
        out.append("C.__new__"); return super().__new__(cls)
    def __init__(self):
        # breakpoint()
        out.append("C.__init__")
# breakpoint()
C()
print(out)
