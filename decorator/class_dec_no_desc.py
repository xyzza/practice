class Deco:
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *a, **k):
        return self.fn(*a, **k)

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # Возвращаем функцию, связанную с экземпляром
        def bound(*args, **kwargs):
            return self.fn(instance, *args, **kwargs)

        return bound


class C:
    @Deco
    def m(self, x):
        return x + 1

print(C().m(1))