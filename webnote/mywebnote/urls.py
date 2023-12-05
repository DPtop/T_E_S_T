from django.urls import path
import mywebnote.views as mynote
from mywebnote.pymain import my_endpoint

urlpatterns = [
    path('login/', mynote.login),
    path('registration/', mynote.registration),
    path('my-endpoint/', my_endpoint, name='my-endpoint'),
    path('first/', mynote.first),   # start page
]
