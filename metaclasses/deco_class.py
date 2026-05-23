breakpoint()
def deco(cls):
    breakpoint()
    cls.tag = (cls.__name__, 'decorated')
    return cls

@deco
class Base:
    breakpoint()
    pass

class Sub(Base):
    breakpoint()
    pass
breakpoint()
print(Base.tag, Sub.tag)
