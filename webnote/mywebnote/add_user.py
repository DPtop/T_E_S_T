import sqlite3
import datetime
from urllib.parse import unquote


nick_name = str('')
pass_word = str('')
e_mail = str('')


def AddUser(request):
    global nick_name, pass_word, e_mail

    will_registered = str(request)
    will_registered = unquote(will_registered, 'utf-8')
    print('will_registered:', will_registered)
    # вычленяем ник и пароль
    i, nname_begin, nname_end, pword_begin, pword_end, email_begin, email_end = 0, 0, 0, 0, 0, 0, 0
    while i < len(will_registered):
        if will_registered[i:i+10] == '?NickName=':
            nname_begin = i + 10
            i += 1
        elif will_registered[i:i+15] == '.end1?Password=':
            nname_end = i
            nick_name = will_registered[nname_begin:nname_end]
            pword_begin = i + 15
            i += 1
        elif will_registered[i:i+12] == '.end2?Email=':
            pword_end = i
            pass_word = will_registered[pword_begin:pword_end]
            email_begin = i + 12
            i += 1
        elif will_registered[i:i+5] == '.end3':
            email_end = i
            e_mail = will_registered[email_begin:email_end]
            i = -1
        # print(i)
        if i == -1:
            break
        else:
            i += 1

    print('nick_name, pass_word, e_mail ::', nick_name, pass_word, e_mail)
    # добавить в таблицу sql
    with sqlite3.connect("db.sqlite3") as db:
        cur = db.cursor()
        cur.execute(f"""
                    INSERT INTO auth_user (password, username, email, last_name, first_name, is_superuser, is_staff, is_active, date_joined) VALUES (
                    '{pass_word}', '{nick_name}', '{e_mail}', '{nick_name}_L', '{nick_name}_F', 0, 1, 1, '{datetime.datetime.now()}'
                    );
                    """)