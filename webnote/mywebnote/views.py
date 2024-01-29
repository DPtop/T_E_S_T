from django.shortcuts import render
from .check_user import CheckUser
from json import dumps
from urllib.parse import unquote

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
    # Открываем и читаем содержимое файла
    with open('mywebnote/static/text/feedback.txt', 'r') as file:
        file_content = file.read()
    # Передаем содержимое файла в контексте шаблона
    encoded_string = file_content.encode('cp1251')
    decoded_string = encoded_string.decode('utf-8')
    context = {'file_content': decoded_string}
    return render(request, "feedback.html", context)  #http://127.0.0.1:8000/mywebnote/feedback/

def some_page(request):
    return render(request, "some_page.html")  #http://127.0.0.1:8000/mywebnote/some_page/
