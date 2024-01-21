from django.shortcuts import render
from .check_user import CheckUser
from json import dumps

# Create your views here.
def login(request):
    dataDictionary = {CheckUser(request): 'CheckUser_request'}
    dataJSON = dumps(dataDictionary)
    return render(request, "login.html", {'data': dataJSON})  # http://127.0.0.1:8000/mywebnote/login/
    # return render(request, "login.html")  # http://127.0.0.1:8000/mywebnote/login/

def registration(request):
    return render(request, "registration.html")  #http://127.0.0.1:8000/mywebnote/registration/

def first(request):
    return render(request, "first.html")  #http://127.0.0.1:8000/mywebnote/first/

def feedback(request):
    return render(request, "feedback.html")  #http://127.0.0.1:8000/mywebnote/feedback/

def main(request):
    return render(request, "main.html")  #http://127.0.0.1:8000/mywebnote/main/
