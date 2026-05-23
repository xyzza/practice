out = []

class A:
    def m(self):
        out.append('A')

class B(A):
    def m(self):
        out.append('B')
        super().m()

class C(A):
    def m(self):
        out.append('C')
        super().m()

class D(B, C):
    def m(self):
        out.append('D')
        super().m()

D().m()
print(out)
