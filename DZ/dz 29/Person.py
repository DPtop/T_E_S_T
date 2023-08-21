class Person:
    def __init__(self, fullName:str='', age:int=0):
        self.__fullName = fullName
        self.__age = age

    def move(self):
        print(f"{self.__fullName} Person идёт")

    def talk(self):
        print(f"{self.__fullName} Person говорит")

    # getter fullName
    @property
    def fullName(self):
        return self.__fullName

    # setter fullName
    @fullName.setter
    def fullName_setter(self, newName):
        self.__fullName = newName

    # getter age
    @property
    def age(self):
        return self.__age

    # setter age
    @age.setter
    def age_setter(self, newAge):
        self.__age = newAge


pers1 = Person('fullio Name', 20)
pers2 = Person('fullx N.A.M.E.', 30)

pers1.move()
pers2.move()
pers1.talk()
pers2.talk()

