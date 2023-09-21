import sqlite3


with sqlite3.connect("dz38.db") as con:
    cur = con.cursor()

    # cur.executescript("""
    #             CREATE TABLE IF NOT EXISTS players (
    #             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    #             name NVARCHAR,
    #             best_score INTEGER
    #             );
    #
    #             CREATE TABLE IF NOT EXISTS games (
    #             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    #             name NVARCHAR,
    #             score INTEGER,
    #             id_player INTEGER,
    #             FOREIGN KEY (id_player) REFERENCES players(id)
    #             );
    #             """)
    #
    # cur.execute("""
    #             INSERT INTO players (name, best_score) VALUES
    #             ("Миша", 200),
    #             ("Ваня", 154),
    #             ("Дима", 178),
    #             ("Коля", 210)
    #             ;
    #             """)
    #
    # cur.execute("""
    #             INSERT INTO games (name, score, id_player) VALUES
    #             ("Миша",110, 1),
    #             ("Миша",200, 1),
    #             ("Дима",178, 3),
    #             ("Коля",10, 4),
    #             ("Коля",30, 4),
    #             ("Коля",40, 4),
    #             ("Ваня",154, 2),
    #             ("Коля",210, 4)
    #             ;
    #             """)


    # таблицы
    print("players")
    result = cur.execute("SELECT * FROM players;")
    for row in result.fetchall():
        print(row)

    print("games")
    result = cur.execute("SELECT * FROM games;")
    for row in result.fetchall():
        print(row)


    # запросы
    # • показать игроков и их кол-во игр
    result = cur.execute("""
    SELECT name, count(name) FROM games GROUP BY id_player;
    """)
    print("\nкол-во игр")
    for row in result.fetchall():
        print(row)

    # • показать игроков и их итоговый счёт за все сыгранные игры
    result = cur.execute("""
    SELECT name, sum(score) FROM games GROUP BY id_player;
    """)
    print("\nитоговый счёт")
    for row in result.fetchall():
        print(row)

    # • Найти общее кол-во игр
    result = cur.execute("""
    SELECT count(id_player) FROM games;
    """)
    print("\nкол-во игр")
    for row in result.fetchall():
        print(row)

    # • Найти худший результат у каждого игрока
    result = cur.execute("""
    SELECT name, min(score) FROM games GROUP BY id_player; 
    """)
    print("\nхудший результат")
    for row in result.fetchall():
        print(row)
