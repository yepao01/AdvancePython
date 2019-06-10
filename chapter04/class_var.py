class A:
    aa = 1
    def __init__(self, x, y): #构造函数
        self.x = x
        self.y = y

a = A(2,3)

A.aa = 11
a.aa = 100
print(a.x, a.y, "a.aa:",a.aa)
print("A.aa:",A.aa)

b = A(3,5)
print("b.aa:",b.aa)

