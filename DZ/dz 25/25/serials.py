class Serials:

    def __init__(self, name, year, actors, director, genre, *seasons):
        self.__name = name          # название сериала
        self.__year = year          # год выхода
        self.__actors = actors      # список актёров
        self.__director = director  # режиссер
        self.__genre = genre        # жанр
        self.__seasons = seasons    # сезоны
        self.name_list = []

    def common_list(self, *cl):     # общий список сериалов
        self.name_list.append(cl)
        return self.name_list

    def search_name_serial(self, sns):  # поиск по названию сериала
        for i in self.name_list:
            if sns in i:
                print('сериал в наличии')
            else: print('сериал отсутствует')
