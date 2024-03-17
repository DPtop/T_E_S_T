import sqlite3
from urllib.parse import unquote


nick_name = str('')
pass_word = str('')
is_loggined = int(0)


def cypher(row1):
    # дешифровка пароля
    dict_code = {'1': '!', '2': '№', '3': '#', '4': '$', '5': '%',
                 '6': '^', '7': '&', '8': '?', '9': '_', '0': '=',
                 'a': '.', 'b': '@', 'c': 'z', 'd': 'y', 'e': 'x',
                 'f': 'w', 'g': 'v', 'h': 'u', 'i': 't', 'j': 's',
                 'k': 'r', 'l': 'q', 'm': 'p', 'n': 'o', 'o': 'n',
                 'p': 'm', 'q': 'l', 'r': 'k', 's': 'j', 't': 'i',
                 'u': 'h', 'v': 'g', 'w': 'f', 'x': 'e', 'y': 'd',
                 'z': 'c', '@': 'b', '.': 'a'}
    cypher_psw = row1
    cypher_psw = cypher_psw[::-1]
    for i in range(len(cypher_psw)):
        list_code = []
        list_code.extend([a == b for a in cypher_psw[i] for b in dict_code.values()])
        for j in list_code:
            if str(j) == 'True':
                cypher_psw = cypher_psw.replace(cypher_psw[i],
                                                list(dict_code.keys())[list(dict_code.values()).index(cypher_psw[i])])
    return cypher_psw


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
            if row[0] == nick_name and cypher(row[1]) == pass_word:
                if is_loggined < 2:
                    user = 'the user is ok'
                    is_loggined += 1
                    return f'{user}, {nick_name}'
                else:
                    is_loggined = 0
            elif nick_name == '' and pass_word == '':
                user = ''
            else:
                user = 'ABSENT'
        return user
