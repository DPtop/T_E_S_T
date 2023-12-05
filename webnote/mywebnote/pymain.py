from django.http import HttpResponse

# получение переменных из js: NickName, ...
def my_endpoint(request):
    print('request:', request)
    return HttpResponse()

##
