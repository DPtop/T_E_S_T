from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")  # http://127.0.0.1:8000/mywebnote/login/

def registration(request):
    return render(request, "registration.html")  #http://127.0.0.1:8000/mywebnote/registration/