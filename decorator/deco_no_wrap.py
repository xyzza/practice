def decoA(fn):
    print(f"decorator A applied")
    def wrap(*a, **k):
        print(f"call A before")
        r = fn(*a, **k)
        print(f"call A after")
        return r
    return wrap

def decoB(fn):
    print(f"decorator B applied")
    def wrap(*a, **k):
        print(f"call B before")
        r = fn(*a, **k)
        print(f"call B after")
        return r
    return wrap


@decoA
@decoB
def f():
    print("f body")

f()
