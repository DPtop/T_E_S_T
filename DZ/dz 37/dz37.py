import sqlite3


with sqlite3.connect("dz37.db") as con:
    cur = con.cursor()

    #cur.execute("DROP TABLE IF EXISTS computers")
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS Salespeople (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                sname NVARCHAR,
                city NVARCHAR,
                comm INTEGER
                );

                CREATE TABLE IF NOT EXISTS Customers (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                cname NVARCHAR,
                city NVARCHAR,
                rating INTEGER,
                id_sp INTEGER,
                FOREIGN KEY (id_sp) REFERENCES Salespeople(id)
                );
                """)

    # cur.execute("""
    #             INSERT INTO Salespeople (sname, city, comm) VALUES
    #             ("Колованов", "Москва", 10),
    #             ("Петров", "Тверь", 25),
    #             ("Плотников", "Москва", 22),
    #             ("Кучеров", "Санкт-Петербург", 28),
    #             ("Малкин", "Санкт-Петербург", 18),
    #             ("Шипачев", "Челябинск", 30),
    #             ("Мозякин", "Одинцово", 25),
    #             ("Проворов", "Москва", 25)
    #             ;
    #             """)
    #
    # cur.execute("""
    #             INSERT INTO Customers (cname, city, rating, id_sp) VALUES
    #             ("Деснов", "Москва", 90, 6),
    #             ("Краснов", "Москва", 95, 7),
    #             ("Кириллов", "Тверь", 96, 3),
    #             ("Ермолаев", "Обнинск", 98, 3),
    #             ("Колесников", "Серпухов", 98, 5),
    #             ("Пушкин", "Челябинск", 90, 4),
    #             ("Лермонтов", "Одинцово", 85, 1),
    #             ("Белый", "Москва", 89, 3),
    #             ("Чудинов", "Москва", 96, 2),
    #             ("Лосев", "Одинцово", 93, 8)
    #             ;
    #             """)
    print("Продавцы")
    result = cur.execute("SELECT * FROM Salespeople;")
    print(result.fetchall())

    print("Покупатели")
    result = cur.execute("SELECT * FROM Customers;")
    print(result.fetchall())


    # Реализовать интерфейс для:
    # - регистрации,
    # - редактирование
    # - и удаления
    # записей о продавцах и заказчиков.

    while True:
        whoami = input("""
1 - продавец
2 - покупатель
3 - выход
Ваш выбор: """)

        if whoami == "3":
            break

        comand = input("""
1 - регистрация
2 - редактирование
3 - удаление
4 - выход 
Ваш выбор: """)

        if comand == "4":
            break

        # Salespeople
        elif whoami == "1":
            # регистрация
            if comand == "1":
                sname = input("Введите имя: ")
                city = input("Укажите город: ")
                comm = int(input("Ваши комиссионные: "))
                cur.execute(f"""
                            INSERT INTO Salespeople (sname, city, comm) VALUES
                            (\'{sname}\', \'{city}\', \'{comm}\');
                            """)
            # редактирование
            elif comand == "2":
                y_id = input("Укажите ваш ID: ")
                whatupd = input("""
1 - имя
2 - город
3 - комиссионные
4 - отмена
Ваш выбор: """)
                if whatupd == "4":
                    break
                elif whatupd == "1":
                    newname = input("Введите имя: ")
                    cur.execute(f"""
                                UPDATE Salespeople SET sname=\'{newname}\' WHERE id=\'{y_id}\';
                                """)
                elif whatupd == "2":
                    newcity = input("Укажите город: ")
                    cur.execute(f"""
                                UPDATE Salespeople SET city=\'{newcity}\' WHERE id=\'{y_id}\';
                                """)
                elif whatupd == "3":
                    newcomm = int(input("Ваши комиссионные: "))
                    cur.execute(f"""
                                UPDATE Salespeople SET comm=\'{newcomm}\' WHERE id=\'{y_id}\';
                                """)
            # удаление
            elif comand == "3":
                y_id = input("Укажите ваш ID: ")
                cur.execute(f"""
                            DELETE FROM Salespeople WHERE id=\'{y_id}\';
                            """)
        ##
        # Customers
        elif whoami == "2":
            # регистрация
            if comand == "1":
                cname = input("Введите имя: ")
                city = input("Укажите город: ")
                rating = int(input("Ваш рейтинг: "))
                id_sp = int(input("ID вашего продавца: "))
                cur.execute(f"""
                            INSERT INTO Customers (cname, city, rating, id_sp) VALUES
                            (\'{cname}\', \'{city}\', \'{rating}\', \'{id_sp}\');
                            """)
            # редактирование
            elif comand == "2":
                y_id = input("Укажите ваш ID: ")
                whatupd = input("""
1 - имя
2 - город
3 - рейтинг
4 - ID продавца
5 - отмена
Ваш выбор: """)
                if whatupd == "5":
                    break
                elif whatupd == "1":
                    newname = input("Введите имя: ")
                    cur.execute(f"""
                                UPDATE Customers SET сname=\'{newname}\' WHERE id=\'{y_id}\';
                                """)
                elif whatupd == "2":
                    newcity = input("Укажите город: ")
                    cur.execute(f"""
                                UPDATE Customers SET city=\'{newcity}\' WHERE id=\'{y_id}\';
                                """)
                elif whatupd == "3":
                    newratg = int(input("Ваш рейтинг: "))
                    cur.execute(f"""
                                UPDATE Customers SET rating=\'{newratg}\' WHERE id=\'{y_id}\';
                                """)
                elif whatupd == "4":
                    newidsp = int(input("ID вашего продавца: "))
                    cur.execute(f"""
                                UPDATE Customers SET id_sp=\'{newidsp}\' WHERE id=\'{y_id}\';
                                """)
            # удаление
            elif comand == "3":
                y_id = input("Укажите ваш ID: ")
                cur.execute(f"""
                            DELETE FROM Customers WHERE id=\'{y_id}\';
                            """)


    ##
    ##
    print("Продавцы")
    result = cur.execute("SELECT * FROM Salespeople;")
    print(result.fetchall())

    print("Покупатели")
    result = cur.execute("SELECT * FROM Customers;")
    print(result.fetchall())

