import sqlite3

with sqlite3.connect("shopIT.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS computers")
    cur.executescript("""
                CREATE TABLE IF NOT EXISTS computers (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                ntype NVARCHAR,
                nbrand NVARCHAR,
                nprice INTEGER
                );
                """)

cur.execute("""
            INSERT INTO computers (ntype, nbrand, nprice) VALUES 
            ("ноутбук", "HP", 101000), 
            ("компьютер", "DNS", 80000),
            ("ноутбук", "ASUS", 151000),
            ("ноутбук", "Huawei", 40000),
            ("ноутбук", "Lenovo", 29999),
            ("компьютер", "Apple", 1)
            ;
            """)

# показать все компьютеры бренда “HP”
# (*усложненный вариант (НЕ ОБЯЗАТЕЛЬНО)
# HP может написано как HP, hp, Hp, Hp
# и в таких случаях все равно запрос должен отобразить все компьютеры
# бренда “HP”)
result = cur.execute("""
                SELECT * FROM computers WHERE nbrand LIKE "hp";
                """)
print(result.fetchall())


# показать компьютеры стоимость которых более 40000
result = cur.execute("""
                SELECT * FROM computers WHERE nprice>40000;
                """)
print(result.fetchall())


# показать компьютеры типа “ноутбук” и стоимостью менее 30000
result = cur.execute("""
                SELECT * FROM computers WHERE ntype="ноутбук" AND nprice<30000;
                """)
print(result.fetchall())

