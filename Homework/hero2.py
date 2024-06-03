class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = fly

    def get_name(self):
        print(f"The hero's name is {self.name}.")

    def double_health(self):
        self.health_points *= 2
        print(f"{self.nickname}'s health points have been doubled to {self.health_points}.")

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}, Fly: {self.fly}"

    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        self.element = "Air"

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        print(f"{self.nickname}'s health points have been squared to {self.health_points}.")

    def true_phrase(self):
        print("True in the True_phrase")


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        self.element = "Earth"

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        print(f"{self.nickname}'s health points have been squared to {self.health_points}.")

    def true_phrase(self):
        print("True in the True_phrase")


class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        self.element = "Space"

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        print(f"{self.nickname}'s health points have been squared to {self.health_points}.")

    def true_phrase(self):
        print("True in the True_phrase")


class Villain(SpaceHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage = self.damage ** 2
        print(f"{self.nickname}'s damage has been squared to {self.damage}.")


# Создание объектов и вызов методов
air_hero = AirHero("Peter Parker", "Spider-Man", "Web-shooting", 150, "With great power comes great responsibility", 50)
earth_hero = EarthHero("Bruce Wayne", "Batman", "High intelligence", 200, "I am Batman", 70)
space_hero = SpaceHero("Hal Jordan", "Green Lantern", "Power ring", 180, "In brightest day, in blackest night", 60)
villain = Villain("Thanos", "Mad Titan", "Infinity Gauntlet", 500, "I am inevitable", 100)

# Применение методов для героев
air_hero.get_name()
air_hero.double_health()
air_hero.true_phrase()
print(str(air_hero))
print(f"Length of catchphrase: {len(air_hero)}")

earth_hero.get_name()
earth_hero.double_health()
earth_hero.true_phrase()
print(str(earth_hero))
print(f"Length of catchphrase: {len(earth_hero)}")

space_hero.get_name()
space_hero.double_health()
space_hero.true_phrase()
print(str(space_hero))
print(f"Length of catchphrase: {len(space_hero)}")

# Применение методов для злодея
villain.get_name()
villain.double_health()
villain.true_phrase()
print(str(villain))
print(f"Length of catchphrase: {len(villain)}")
villain.crit()
