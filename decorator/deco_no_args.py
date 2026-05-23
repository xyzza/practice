def deco(func=None, *, prefix='>'):
    if func is None:
        def wrap(fn):
            def inner(*a, **k):
                print(prefix + fn.__name__)
                return fn(*a, **k)
            return inner
        return wrap
    else:
        def inner(*a, **k):
            print(prefix + func.__name__)
            return func(*a, **k)
        return inner

@deco
def f(): pass

@deco(prefix='*')
def g(): pass

f(); g()
