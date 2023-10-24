from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_dz_url(request):   # http://127.0.0.1:8000/dz47url/
    return HttpResponse('Страница ДЗ 47 !')
