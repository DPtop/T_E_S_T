import sqlite3
from urllib.parse import unquote


nick_name = str('')
pass_word = str('')
is_loggined = int(0)


def CheckUser(request):
    global nick_name, pass_word, is_loggined

    is_registered = str(request)
    is_registered = unquote(is_registered, 'utf-8')
    # вычленяем ник и пароль
    i, nname_begin, nname_end, pword_begin, pword_end = 0, 0, 0, 0, 0
    while i < len(is_registered):
        if is_registered[i:i+10] == '?NickName=':
            nname_begin = i + 10
            i += 1
        elif is_registered[i:i+15] == '.end1?Password=':
            nname_end = i
            nick_name = is_registered[nname_begin:nname_end]
            pword_begin = i + 15
            i += 1
        elif is_registered[i:i+5] == '.end2':
            pword_end = i
            pass_word = is_registered[pword_begin:pword_end]
            i = -1
        if i == -1:
            break
        else:
            i += 1

    # проверка наличия в таблице sql
    with sqlite3.connect("db.sqlite3") as db:
        cur = db.cursor()
        result = cur.execute("SELECT username, password FROM auth_user;")
        for row in result.fetchall():
            if row[0] == nick_name and row[1] == pass_word:
                if is_loggined < 2:
                    user = 'the user is ok'
                    is_loggined += 1
                    return user
                else:
                    is_loggined = 0
            elif nick_name == '' and pass_word == '':
                user = ''
            else:
                user = 'ABSENT'
        return user
