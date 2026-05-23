breakpoint()
class D:
    def __init__(self, name):
        breakpoint()
        self.name = name
    def __get__(self, instance, owner=None):
        breakpoint()
        return f"{'inst' if instance is not None else 'class'}:{self.name}"

class Meta(type):
    breakpoint()
    y = D('y')

class C(metaclass=Meta):
    breakpoint()
    x = D('x')

breakpoint()
print(C.x, C.y)
