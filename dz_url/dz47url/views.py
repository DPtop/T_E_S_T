from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_dz_url(request):   # http://127.0.0.1:8000/dz47url/
    return HttpResponse('Страница ДЗ 47 !')

def index_dz_html(request):  # http://127.0.0.1:8000/dz47url/dz48/
    menulist = ('1) ...', '2) ...', '3) ...', '4) и т.д.')
    data = {'title': 'Site according to dz48',
            'menu': menulist}
    return render(request, 'dz48site.html', data)
