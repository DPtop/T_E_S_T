import sqlite3
from classes import *

bnk = Bank
crr = Currency

while True:
    choose = input('''
1. Добавить пользователя
2. Открытие счёта
3. Просмотр учётной записи
4. Выход
>> ''')

    with sqlite3.connect("bankdb.db") as con:
        cur = con.cursor()
        # Выход
        if choose == '4':
            break
        # Добавить пользователя
        elif choose == '1':
            fs_name = input('Ведите имя и фамилию: ')
            mail_code = int(input('Укажите почтовый код: '))
            name_first = fs_name.split(' ')[0]
            name_second = fs_name.split(' ')[1]
            bnk(name_first, name_second, mail_code)
        # Открытие счёта
        elif choose == '2':
            id_acc = int(input('id пользователя: '))
            open_account = input('Валюта (Dollar, Pound, Rupee): ')
            crr(open_account, id_acc)
        # Просмотр учётной записи
        elif choose == '3':
            result_bnk = cur.execute("SELECT * FROM BankDB;")
            for row_bnk in result_bnk.fetchall():
                print(f'[{row_bnk[0]}]', *row_bnk[1:], end=' ')
                result_crr = cur.execute(f"SELECT open_account FROM Currency WHERE id_acc={row_bnk[0]};")
                for row_crr in result_crr.fetchall():
                    print(*row_crr, end=' ')
                print()
