import sqlite3
from django.http import HttpResponse
from urllib.parse import unquote


nick_name = str('')
pass_word = str('')
is_registered = str('')


def CheckUser(request):
    global is_registered, nick_name, pass_word
    is_registered = request     # unquote(request, 'utf-8')
    print('request :: ', is_registered)
    # вычленяем ник и пароль
    i, nname_begin, nname_end, pword_begin, pword_end = 0, 0, 0, 0, 0
    while i < len(is_registered):
        if is_registered[i:i+10] == '?NickName=':
            nname_begin = i + 10
            i += 1
        elif is_registered[i:i+15] == '.end1?Password=':
            nname_end = i
            nick_name = unquote(is_registered[nname_begin:nname_end], 'utf-8')
            # nick_name = is_registered[nname_begin:nname_end]
            pword_begin = i + 15
            i += 1
        elif is_registered[i:i+5] == '.end2':
            pword_end = i
            pass_word = unquote(is_registered[pword_begin:pword_end], 'utf-8')
            # pass_word = is_registered[pword_begin:pword_end]
        i += 1
    # проверка наличия в таблице sql
    with sqlite3.connect("db.sqlite3") as db:
        cur = db.cursor()
        result = cur.execute("SELECT * FROM mywebnote_users;")
        ok = False
        for row in result.fetchall():
            # print(':2:', 'id:', row[0], ', n:', row[1], ', p:', row[2])
            if row[1] == nick_name and row[2] == pass_word:
                print('the user is ok')
                ok = True
        if not ok:
            print('NO')
    return HttpResponse()
