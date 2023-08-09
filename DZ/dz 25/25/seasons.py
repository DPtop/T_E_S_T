class Seasons:

    def __init__(self, name, series_number, *series_list):
        self.__name = name                      # название сезона
        self.__series_number = series_number    # кол-во серий
        self.__series_list = series_list        # список серий
        self.list_seasons = []
        self.list_series = []

    def list_name_seasons(self, *lns):      # список названий сезонов
        self.list_seasons.append(lns)
        return self.list_seasons

    def search_name_season(self, sns):      # поиск по названию сезона
        for i in self.list_seasons:
            print('сезон в наличии') if sns in i else print('сезон отсутствует')

    def search_series_list(self, ssl):      # поиск по номеру серии
        yes = False
        for i in self.__series_list:
            if ssl in i:
                print('серия в наличии')
                yes = True
        if not yes:
            print('серия отсутствует')
