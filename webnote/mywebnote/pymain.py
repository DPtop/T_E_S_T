from django.http import HttpResponse
from urllib.parse import unquote
import sqlite3


# получение из js: feedback
comm_from, comm_to = 0, 0
def feed_back(request):
    # global comm_from, comm_to
    # decode = unquote(str(request), 'cp1251')
    # # выдёргиваем нужное
    # comm_start = "?feedtext="
    # comm_end = ".end"
    # comm_nextline = '<br>'
    # i = 0
    # while i < len(decode):
    #     if decode[i:i+10] == comm_start:
    #         comm_from = i + 10
    #     if decode[i:i+4] == comm_end:
    #         comm_to = i
    #     if decode[i:i+4] == comm_nextline:
    #         # запись до знака новой строки
    #         comm_save = decode[comm_from:i]
    #         with open('mywebnote/static/text/feedback.txt', 'a') as file_feedback:
    #             file_feedback.write('\t' + comm_save + '\n')
    #         comm_from = i + 4
    #     i += 1
    # comm_save = decode[comm_from:comm_to]
    # # последняя запись
    # with open('mywebnote/static/text/feedback.txt', 'a') as file_feedback:
    #     file_feedback.write('\t' + comm_save + '\n\n')

    ##  db вместо feedback.txt
    global comm_from, comm_to
    decode = unquote(str(request), 'cp1251')
    # выдёргиваем нужное
    comm_start = "?feedtext="
    comm_end = ".end"
    nick = ''
    comm_nick = ':<br>'
    i = 0
    while i < len(decode):
        if decode[i:i+10] == comm_start:
            comm_from = i + 10
        if decode[i:i+4] == comm_end:
            comm_to = i

        if decode[i:i+5] == comm_nick:
            comm_save = decode[comm_from:i]
            nick = comm_save
            comm_from = i + 5
        i += 1
    comm_save = decode[comm_from:comm_to]
    # запись
    comm_text = comm_save
    with sqlite3.connect("db.sqlite3") as db:
        cur = db.cursor()
        cur.execute(f"""
                        INSERT INTO mywebnote_feedbackdb (nickname, text) VALUES (
                        '{nick}', '{comm_text}'
                        );
                        """)
    ##
    return HttpResponse()
