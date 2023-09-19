import sqlite3

with sqlite3.connect("dz35.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS computers")
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

cur.execute("""
            INSERT INTO Salespeople (sname, city, comm) VALUES 
            ("Колованов", "Москва", 10), 
            ("Петров", "Тверь", 25),
            ("Плотников", "Москва", 22),
            ("Кучеров", "Санкт-Петербург", 28),
            ("Малкин", "Санкт-Петербург", 18),
            ("Шипачев", "Челябинск", 30),
            ("Мозякин", "Одинцово", 25),
            ("Проворов", "Москва", 25)
            ;
            """)

cur.execute("""
            INSERT INTO Customers (cname, city, rating, id_sp) VALUES 
            ("Деснов", "Москва", 90, 6),
            ("Краснов", "Москва", 95, 7),
            ("Кириллов", "Тверь", 96, 3),
            ("Ермолаев", "Обнинск", 98, 3),
            ("Колесников", "Серпухов", 98, 5),
            ("Пушкин", "Челябинск", 90, 4),
            ("Лермонтов", "Одинцово", 85, 1),
            ("Белый", "Москва", 89, 3),
            ("Чудинов", "Москва", 96, 2),
            ("Лосев", "Одинцово", 93, 8)
            ;
            """)

