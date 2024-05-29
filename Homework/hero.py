# 1)создать класс SuperHero с cвойством класса people='people'
class SuperHero:
    # 1) свойство класса
    people = 'people'

    # 2)создать конструктор класса(init) с атрибутами name,nickname,superpower,health_points, catchphrase
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    # 3)создать метод который выводит имя героя

    def get_name(self):
        print(f"The hero's name is {self.name}.")

    # 4)создать метод который умножает здоровье героя на 2
    def double_health(self):
        self.health_points *= 2
        print(f"{self.nickname}'health points multiplies double {self.health_points}.")

# 5) cоздать магический метод который выводит прозвище героя,его суперспособность и его здоровье

    def __str__(self):
        return (f'Nickname: {self.nickname}\n'
                f'Superpower: {self.superpower}\n'
                f'Health Points : {self.health_points}\n'
                f'----------------------------------\n')

# 6) создать магический метод который считает длину коронной фразы героя

    def __len__(self):
        return len(self.catchphrase)

# 7)создать объект класса Hero и применить все методы которые вы создали

hero = SuperHero('Scarlett Johansson', 'Black Widow', 'stamina', 1000, "I've got red in my ledger")

# Применение всех методов
hero.get_name()
hero.double_health()

print(str(hero))
print(f"The length of the catchphrase is: {len(hero)} characters.")



