from django.http import HttpResponse
def my_endpoint(request):
    print('request:', request)
    return HttpResponse()

##
