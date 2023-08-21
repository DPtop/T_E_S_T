'''пример Абстрактного класса'''
#
class Wood:
    def __init__(self, *wood):
        self.__woods = wood

    def woods(self):
        return self.__woods

#
class Abstract(Wood):
    def showChoice(self):
        print('В наличии:', end=' ')
        for i in wood.woods():
            if wood.woods()[-1] == i:
                print(i, end='.')
            else:
                print(i, end=', ')


wood = Wood('берёза', 'дуб', 'сосна', 'клён')
abstract = Abstract()

abstract.showChoice()

