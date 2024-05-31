# принципы ооп
# 1 - принцип - Наследование
# 2 - принцип - Полиморфизм - изменение поведения унаследованных методов
# 3 - принцип - Инкапсуляция
# 4 - принцип - Абстракция
#
# git .gitignore



# супер класс \ родительский класс
class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def describe_car(self):
        print('model- ',self.model)
        super().describe_car()
    def new(self):
        self.describe_car()


    def __str__(self):
        return (f"---------\n"
                f"year:{self.year}\n"
                f"make: {self.make}\n"
                f"model: {self.model}\n"
                f"----------")

car1=Car("Ford","Ford",2020, 'black')
car2=Car("Ford","Ford",2020, 'black')
car3=Car("Ford","Ford",2020, 'black')
car4=Car("Ford","Ford",2020, 'black')
car5=Car("Ford","Ford",2020, 'black')
car6=Car("Ford","Ford",2020, 'black')
car7=Car("Ford","Ford",2020, 'black')
print(car1)
# car1.describe_car()

# DRY

# дочерний класс
#

class Car2(Car):
    pass

c=Car2('Ford','Ford',2020, 'black')
print(c)
c.describe_car()
# полиморфизм-изменение поведения унаследованных методов

class Car3(Car2):
    def __init__(self,make,model,year,color):
        super().__init__(make,model,year,color)
        Car2.__init__(self,make,model,year,color)
        self.color = color

    def describe_car(self):
        print('color: ',self.color)

c1=Car3('BMW','m5',2022,'black')
print(c1)
# c1.describe_car()

