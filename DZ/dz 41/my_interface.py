from Poison import Poison
import sqlite3


while True:
    choose = input("""\nМеню:
    1 - добавить
    2 - показать
    3 - изменить
    4 - удалить
    5 - выход
>> """)
    # отмена
    if choose == '5':
        break
    choose_db = Poison()
    with sqlite3.connect("poisons.db") as con:
        cur = con.cursor()
        # добавить
        if choose == '1':
            choose_db.name = input("название: ")
            choose_db.price = int(input("цена: "))
            choose_db.items_to_create = input("ингредиенты <item_num>: ")
            choose_db.DB_poisons()
        # показать
        elif choose == '2':
            choose_db.show_poisons
        # изменить
        elif choose == '3':
            id_change = int(input('укажите id: '))
            choose_change = input("""Что изменить:
    1 - название
    2 - цена
    3 - ингредиенты
    4 - отмена
>> """)
            if choose_change == '4':
                break
            if choose_change == '1':
                new_name = input('новое название: ')
                cur.execute(f"""
                            UPDATE Poisons SET name=\'{new_name}\' WHERE id=\'{id_change}\';
                            """)
            elif choose_change == '2':
                new_price = input('новая цена: ')
                cur.execute(f"""
                            UPDATE Poisons SET price=\'{new_price}\' WHERE id=\'{id_change}\';
                            """)
            elif choose_change == '3':
                new_items_to_create = input('новые ингредиенты <item_num>: ')
                cur.execute(f"""
                            UPDATE Poisons SET items_to_create=\'{new_items_to_create}\' WHERE id=\'{id_change}\';
                            """)
        # удалить
        elif choose == '4':
            id_change = int(input('укажите id для удаления: '))
            cur.execute(f"""
                        DELETE FROM Poisons WHERE id=\'{id_change}\';
                        """)

