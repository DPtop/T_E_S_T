from django.shortcuts import render
from .check_user import CheckUser
from json import dumps
from urllib.parse import unquote
import sqlite3

# Create your views here.
def login(request):
    # Передача в js после проверки в .py
    dataDictionary = {CheckUser(request): 'CheckUser_request'}
    dataJSON = dumps(dataDictionary)
    return render(request, "login.html", {'data': dataJSON})  # http://127.0.0.1:8000/mywebnote/login/

def registration(request):
    return render(request, "registration.html")  #http://127.0.0.1:8000/mywebnote/registration/

def first(request):
    NickName = request.GET.get('NickName')
    return render(request, "first.html", {'NickName': NickName})  #http://127.0.0.1:8000/mywebnote/first/

def feedback(request):
    # # Открываем и читаем содержимое файла
    # with open('mywebnote/static/text/feedback.txt', 'r') as file:
    #     file_content = file.read()
    # # Передаем содержимое файла в контексте шаблона
    # encoded_string = file_content.encode('cp1251')
    # decoded_string = encoded_string.decode('utf-8')
    # context = {'file_content': decoded_string}      # текст передаётся в теге <pre>file_content</pre>
    # return render(request, "feedback.html", context)  #http://127.0.0.1:8000/mywebnote/feedback/
    ##
    #  db вместо feedback.txt
    with sqlite3.connect("db.sqlite3") as db:
        cur = db.cursor()
        # посмотреть
        result = cur.execute("SELECT nickname, text FROM mywebnote_feedbackdb;")
        row_dict = {}
        row_str_fin = ''
        for row in result.fetchall():
            row_str = f'\t{row[0]}:\n\t{row[1]}'
            encoded_string = row_str.encode('cp1251')
            decoded_string = encoded_string.decode('utf-8')
            decoded_string = decoded_string.replace('<br>', '\n\t')
            row_str_fin += decoded_string
            row_dict = {'file_content': row_str_fin}
        return render(request, "feedback.html", row_dict)  #http://127.0.0.1:8000/mywebnote/feedback/

def some_page(request):
    return render(request, "some_page.html")  #http://127.0.0.1:8000/mywebnote/some_page

def dish_order(request):
    return render(request, "dish_order.html")  #http://127.0.0.1:8000/mywebnote/dish_order/

def recover(request):
    return render(request, "recover.html")  #http://127.0.0.1:8000/mywebnote/recover/