from serials import *
from seasons import *


# #
# class Serials
# #

# ввод данных о сериалах
sl1 = Serials('название-сериала-1', 1, 'актёр-1, актёр-2', 'режисёр-1', 'жанр-1', 'сезон-1', 'сезон-2')
sl2 = Serials('название-сериала-2', 3, 'актёр-3, актёр-4', 'режисёр-2', 'жанр-2', 'сезон-01')

# общий список сериалов
common_serials = sl1.common_list(sl1._Serials__name, sl2._Serials__name)
print(common_serials)

# поиск по названию сериала
sl1.search_name_serial(input('сериал<< '))


# #
# class Seasons
# #

# ввод данных о сезонах
seasons1_1 = Seasons('сезон-1', 10, 'с1', 'с2', 'с3', 'с4', 'с5', 'с6', 'с7', 'с8', 'с9', 'с10')
seasons1_2 = Seasons('сезон-2', 2, 'с1', 'с2')
seasons2 = Seasons('сезон-01', 8, 'с1', 'с2', 'с3', 'с4', 'с5', 'с6', 'с7', 'с8')

# поиск по названию сезона
seasons1_1.list_name_seasons(seasons1_1._Seasons__name, seasons1_2._Seasons__name, seasons2._Seasons__name)
season_match = input('сезон<< ')
seasons1_1.search_name_season(season_match)

# поиск по номеру серии в сезоне (season_match)
match season_match:
    case 'сезон-1': seasons1_1.search_series_list(input('номер_серии<< '))
    case 'сезон-2': seasons1_2.search_series_list(input('номер_серии<< '))
    case 'сезон-01': seasons2.search_series_list(input('номер_серии<< '))

