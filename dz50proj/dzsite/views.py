from django.shortcuts import render

# Create your views here.
def pages(request, npage):
    data = {
        'menu': ['default', 'page_1']
    }
    if npage in ['def', 'default', 'page_1']:
        if npage == 'def':
            npage = 'default'
        return render(request, f'html/{npage}.html', data)
