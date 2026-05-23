def D(label):
    print(f"decorator {label} evaluated")
    def deco(fn):
        print(f"decorator {label} applied")
        def wrap(*a, **k):
            print(f"call {label} before")
            r = fn(*a, **k)
            print(f"call {label} after")
            return r
        return wrap
    return deco

@D('A')
@D('B')
def f():
    print("f body")

f()
