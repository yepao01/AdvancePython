#新式类

class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)



"""
class A:
    name = "A"
    def __init__(self):
        self.name = 'obj'

a = A()
print("a.name:",a.name)
print('A.name:',A.name)

"""

















