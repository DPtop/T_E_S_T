import sqlite3
from urllib.parse import unquote
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail
from mywebnote.check_user import cypher


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
            # дешифровка эмейла
            dict_code = {'1': '!', '2': '№', '3': '#', '4': '$', '5': '%',
                         '6': '^', '7': '&', '8': '?', '9': '_', '0': '=',
                         'a': '.', 'b': '@', 'c': 'z', 'd': 'y', 'e': 'x',
                         'f': 'w', 'g': 'v', 'h': 'u', 'i': 't', 'j': 's',
                         'k': 'r', 'l': 'q', 'm': 'p', 'n': 'o', 'o': 'n',
                         'p': 'm', 'q': 'l', 'r': 'k', 's': 'j', 't': 'i',
                         'u': 'h', 'v': 'g', 'w': 'f', 'x': 'e', 'y': 'd',
                         'z': 'c', '@': 'b', '.': 'a'}
            cypher_eml = ''
            cypher_eml_row1 = row[1]
            for i in range(len(row[1])):
                cypher_eml += dict_code[cypher_eml_row1[i]]
            cypher_eml = cypher_eml[::-1]
            #
            psw = cypher(row[2])
            #
            if row[0] == nick_name and cypher_eml == e_mail:
                # # Настройки SMTP сервера
                # smtp_server = 'smtp.mail.ru'
                # smtp_port = 587
                # smtp_username = 'dyomdiftest@mail.ru'
                # smtp_password = '41PhY7Grn4d2xt07N4hd'
                # # Создание сообщения
                # sender_email = 'dyomdiftest@mail.ru'
                # receiver_email = row[1]
                # subject = 'Password Recovering'
                # body = row[2]
                # #
                # message = MIMEMultipart()
                # message['From'] = sender_email
                # message['To'] = receiver_email
                # message['Subject'] = subject
                # message.attach(MIMEText(body, 'plain'))
                # # Отправка письма
                # with smtplib.SMTP(smtp_server, smtp_port) as server:
                #     server.starttls()
                #     server.login(smtp_username, smtp_password)
                #     text = message.as_string()
                #     server.sendmail(sender_email, receiver_email, text)
                send_mail(  # меньше строк, но + настройки в settings
                    'Subject: Password Recovering',
                    psw,
                    'dyomdiftest@mail.ru',
                    [cypher_eml],
                    fail_silently=False,
                )
