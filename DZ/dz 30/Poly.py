'''пример Множественного наследования'''
#
class Wood:
    def __init__(self, *wood):
        self.__woods = wood

    def woods(self):
        print('В наличии:', end=' ')
        for i in self.__woods:
            if self.__woods[-1] == i:
                print(i, end='.')
            else:
                print(i, end=', ')

#
class Stone:
    def __init__(self, *stone):
        self.__stones = stone

    def stones(self):
        print('В наличии:', end=' ')
        for i in self.__stones:
            if self.__stones[-1] == i:
                print(i, end='.')
            else:
                print(i, end=', ')

#
class Poly(Wood, Stone):
    def showChoice(self):
        choice = input('Выберите материал (дерево|камень): ')
        if choice == 'дерево':
            wood.woods()
        elif choice == 'камень':
            stone.stones()

##
wood = Wood('берёза', 'дуб', 'сосна', 'клён')
stone = Stone('гранит', 'мрамор', 'алмаз', 'сапфир')
poly = Poly()

poly.showChoice()

