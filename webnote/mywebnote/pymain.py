from django.http import HttpResponse
from urllib.parse import unquote


# получение переменных из js: NickName, ...
def my_logreg(request):
    # print('request:', request)
    return HttpResponse()


# получение из js: feedback
comm_from, comm_to = 0, 0
def my_textarea(request):
    decode = unquote(str(request), 'cp1251')
    # выдёргиваем нужное
    comm_start = "?feedtext="
    comm_end = ".end"
    comm_nextline = '<br>'
    i = 0
    global comm_from, comm_to
    while i < len(decode):
        if decode[i:i+10] == comm_start:
            comm_from = i + 10
        if decode[i:i+4] == comm_end:
            comm_to = i
        if decode[i:i+4] == comm_nextline:
            # запись до знака новой строки
            comm_save = decode[comm_from:i]
            with open('mywebnote/static/text/feedback.txt', 'a') as file_feedback:
                file_feedback.write('\t' + comm_save + '\n')
            comm_from = i + 4
        i += 1
    comm_save = decode[comm_from:comm_to]
    # последняя запись
    with open('mywebnote/static/text/feedback.txt', 'a') as file_feedback:
        file_feedback.write('\t' + comm_save + '\n\n')
    return HttpResponse()

##
