import sqlite3

class Bank:
    def __init__(self, name_first:str, name_second:str, mail_code:int):
        if type(name_first) is not str:
            raise "Не соответствует заявленному типу 'name_first:str'."
        if type(name_second) is not str:
            raise "Не соответствует заявленному типу 'name_second:str'."
        if type(mail_code) is not int:
            raise "Не соответствует заявленному типу 'mail_code:int'."

        self.__name_first = name_first
        self.__name_second = name_second
        self.__mail_code = mail_code

        with sqlite3.connect("bankdb.db") as con:
            cur = con.cursor()
            # table Bank DB
            cur.executescript("""
                            CREATE TABLE IF NOT EXISTS BankDB (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            name_first TEXT,
                            name_second TEXT,
                            mail_code INTEGER
                            );
                            """)
            # insert in Bank DB
            cur.execute(f"""
                        INSERT INTO BankDB (name_first, name_second, mail_code) VALUES
                        ('{self.__name_first}', '{self.__name_second}', {self.__mail_code})
                        ;
                        """)

class Currency:
    def __init__(self, open_account:str, id_acc:int):
        currency = ['Dollar', 'Pound', 'Rupee']
        if open_account not in currency:
            raise "Не соответствует заявленной валюте: Dollar, Pound, Rupee."
        if type(id_acc) is not int:
            raise "Не соответствует заявленному типу 'id_acc:int'."
        self.__open_account = open_account

        with sqlite3.connect("bankdb.db") as con:
            cur = con.cursor()
            # table Currency
            cur.executescript("""
                               CREATE TABLE IF NOT EXISTS Currency (
                               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                               open_account  TEXT,
                               id_acc INTEGER,
                               FOREIGN KEY (id_acc) REFERENCES BankDB(id)
                               );
                               """)
            # insert in Currency
            cur.execute(f"""
                           INSERT INTO Currency (open_account, id_acc) VALUES
                           ('{self.__open_account}', '{id_acc}')
                           ;
                           """)
