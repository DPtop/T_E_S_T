# башня
class Tower:
    def __init__(self, armor:int, health:int):
        self.__armor = armor
        self.__health = health

    @property
    def armor(self):
        return self.__armor

    @property
    def health(self):
        return self.__health

    # перегрузка '+' __add__
    def __add__(self, other):
        # max доп.броня_башни/armor = 50 единиц; max целостность_башни/health = 100 единиц
        return Tower(self.__armor + other.armor if (self.__armor + other.armor) < 50 else 50,
                     self.__health + other.health if (self.__health + other.health) < 100 else 100)

    # перегрузка '-' __sub__
    def __sub__(self, other):
        # атака по броне = 50% от атаки; атака по башне = 100% от атаки
        # впервую очередь атака по броне до 0 единиц, затем по башне
        # если во время атаки: armor < 0, e.g. -10, then health attack = |-10|*2 # где *2 -- возврат к 100% атаки
        return Tower(0 if (self.__armor - other.attack/2) < 0 else self.__armor - other.attack/2,
                     self.__health - abs((self.__armor - other.attack/2)*2)
                     if (self.__armor - other.attack/2) <= 0 else self.__health - 0)

#
#

# стрелковая башня
class AttackTower(Tower):
    def __init__(self, attack:int, armor:int, health:int):
        self.__attack = attack
        super().__init__(armor, health)

    @property
    def attack(self):
        return self.__attack


#
#

tower = Tower(20, 60)
heal_armor = Tower(5, 0)
heal_health = Tower(0, 15)
attack = AttackTower(50, 5, 25)

while True:
    print('БАШНЯ доп.броня/целостность:', tower.armor, "..", tower.health)

    print('''\nукажите номер действия:
    1. атаковать стрелковой башней
    2. добавить брони
    3. ремонт башни''')
    action = int(input('<< '))

    match action:
        case 1: tower = tower - attack
        case 2: tower = tower + heal_armor
        case 3: tower = tower + heal_health

    if tower.health <= 0:
        print('башня повержена')
        break

