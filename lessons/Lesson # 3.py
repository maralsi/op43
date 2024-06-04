#
# # 4 наследование полиморфизм
# #
#
# class Big0:
#     def __init__(self): ...
#
#     def res(self):
#         print ('метод класса 1')
#
# сlass Big02(Big0):
#     def __init__(self): ...
#     def res(self):
#         print('метод класса 2')
#         super().res()
#
# a=Big0()
# b=Big01()
# a.res()
# b.res()

# уровни доступа, всего = 3
# 1 - публичный
# 2 - защищенный отличается _
# 3 - скрытый __

class Bank(object):
    def __init__(self, name, balance, pin, svv):
        self.name = name
        self.__balance = balance
        self._pin = pin
        self.svv = svv

   def setpin(self, other):
        self._pin = other
   def getpin(self):
        return self._pin

    def result(self):
        print(self._pin, self.svv)

    def __str__(self):
        return f'{self.name} {self.__balance}'

beka=Bank('beka', 1000, 2525, 644)
beka1=Bank('beka', 1000, 2525, 644)

print(beka,
      beka.result())
setpin(beka)
# beka.result()
# print(beka)
# beka.balance = 1000000
# print(beka)
# beka.__balance = 1000000000
# print(beka)

beka.__balance = 1000000000
beka._Bank__balance = 1000
# print(dir(beka))
print(beka.__balance)

beka.__balance=100000000
beka._Bank__balance = 75
# print(dir(beka))
print(beka)

# beka.pin=6666
# beka.age=28
# print(dir(beka))
# beka.balance=100000
# beka.result()

class Person(Bank):pass

cl=Person('cl', 1000, 2525, 644)
print(dir(cl))

print(Person.mro())



