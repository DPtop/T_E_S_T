# class

class Computer:
    def __init__(self, comp_type:str='', RAM:int=0, processor:str='', price:int=0):
        self.__comp_type = comp_type
        self.__RAM = RAM
        self.__processor = processor
        self.__price = price


    def show_all(self):
        print(self.__comp_type, self.__RAM, self.__processor, self.__price)

    @property
    def get_comp_type(self):
        return self.__comp_type

    @property
    def get_RAM(self):
        return self.__RAM

    @property
    def get_price(self):
        return self.__price

