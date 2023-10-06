import sqlite3

class Poison:
    def __init__(self, name:str='', price:int=0, items_to_create:list=()):
        self.check_types(name, price)
        self.__name = name
        self.__price = abs(price)
        self.__items_to_create = items_to_create

    def check_types(self, name, price):
        if type(name) is not str:
            raise "Не соответствует заявленному типу: str(name)"
        if type(price) is not int:
            raise "Не соответствует заявленному типу: int(price)"

    # name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # price
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    # items_to_create
    @property
    def items_to_create(self):
        return self.__items_to_create
    @items_to_create.setter
    def items_to_create(self, new_item):
        self.__items_to_create = new_item

## COMMIT 2
    # DB
    def DB_poisons(self):
        self.check_types(self.__name, self.__price)
        with sqlite3.connect("poisons.db") as con:
            cur = con.cursor()
            # cur.execute("DROP TABLE IF EXISTS Poisons")  # drop table
            cur.executescript("""
                            CREATE TABLE IF NOT EXISTS Poisons (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            name NVARCHAR,
                            price INTEGER,
                            items_to_create NVARCHAR
                            );
                            """)

            cur.execute(f"""
                            INSERT INTO Poisons (name, price, items_to_create) VALUES
                            ('{self.__name}', {self.__price}, '{self.__items_to_create}')
                            ;
                            """)
            # for row in result.fetchall():
            #     print(row)

    # show
    @property
    def show_poisons(self):
        with sqlite3.connect("poisons.db") as con:
            cur = con.cursor()
            result = cur.execute("SELECT * FROM Poisons;")
            for row in result.fetchall():
                # print('\n', row)
                print(f'{row[0]}. {row[1]}', end=' (')
                row_split = str(row[3]).split('_')
                for i in range(len(row_split)):
                    if i % 2 == 0:
                        print(row_split[i], end=' ')
                    else:
                        if i != len(row_split)-1:
                            print(f'{row_split[i]}шт', end=' + ')
                        else:
                            print(f'{row_split[i]}шт)')


# p1 = Poison()
# p1.name = "pois1"
# p1.price = 123
# p1.items_to_create = 'item1_2'
# #
# p2 = Poison()     #!
# p2.name = "pois2"
# p2.price = 234
# p2.items_to_create = 'item2.1_1_item2.2_3'
# #
# p1.DB_poisons()
# p2.DB_poisons()
# #
# p2.show_poisons     #!
