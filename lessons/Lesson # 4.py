
# множественное наследование

class A:
    def __init__(self, name, balance, pin, svv):
        self.name =name
        self.balance = balance
        self.pin = pin
        self.svv = svv

class B(A):
    def a(self):
        print ('метод класса В')


class C:
    def __init__(self, key):
        self.key = key
    def a(self):
        print('метод С')

# MRO - порядок выполненя методов

class D(B,C):
    def A(self):
        print('метод D')

print(dir(D))

d=D('beka', 100000, 100, 1000)
d.a()
# d.c()
# p=B()
# p.a()
# p.b()

print(D.mro())





