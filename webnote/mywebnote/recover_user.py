import sqlite3
from urllib.parse import unquote
from django.core.mail import send_mail


nick_name = str('')
e_mail = str('')


def RecoverUser(request):
    global nick_name, e_mail

    recoverUser = str(request)
    recoverUser = unquote(recoverUser, 'utf-8')
    # вычленяем ник и эмейл
    i, nname_begin, nname_end, e_mail_begin, e_mail_end = 0, 0, 0, 0, 0
    while i < len(recoverUser):
        if recoverUser[i:i+10] == '?NickName=':
            nname_begin = i + 10
            i += 1
        elif recoverUser[i:i+12] == '.end1?Email=':
            nname_end = i
            nick_name = recoverUser[nname_begin:nname_end]
            e_mail_begin = i + 12
            i += 1
        elif recoverUser[i:i+5] == '.end2':
            e_mail_end = i
            e_mail = recoverUser[e_mail_begin:e_mail_end]
            i = -1
        if i == -1:
            break
        else:
            i += 1

    # проверка наличия в таблице sql и отправка
    with sqlite3.connect("db.sqlite3") as db:
        cur = db.cursor()
        result = cur.execute("SELECT username, email, password FROM auth_user;")
        for row in result.fetchall():
            if row[0] == nick_name and row[1] == e_mail:
                print('row:1:', row[1], row[2])
                # send_mail(
                #     'Password Recovering',
                #     f'{row[2]}',
                #     'example@mail',   # ot
                #     [f'{row[1]}'],    # to
                #     fail_silently=False,
                # )
                # print('row:2:', row[1], row[2])