import sqlite3
from django.http import HttpResponse
from urllib.parse import unquote


nick_name = str('')
pass_word = str('')


def CheckUser(request):
    print('request :: ', request)
    global nick_name, pass_word
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
        i += 1
    print('::', nick_name, pass_word)
    # проверка наличия в таблице sql
    with sqlite3.connect("db.sqlite3") as db:
        cur = db.cursor()
        result = cur.execute("SELECT * FROM mywebnote_users;")
        ok = False
        for row in result.fetchall():
            # print(':sql:', 'id:', row[0], ', n:', row[1], ', p:', row[2])
            if row[1] == nick_name and row[2] == pass_word:
                print('the user is ok')
                ok = True
        if not ok:
            print('NO')
    nick_name = pass_word = ''
    # return HttpResponse()
