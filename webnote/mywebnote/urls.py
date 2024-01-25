from django.urls import path
import mywebnote.views as mynote
from mywebnote.pymain import my_textarea
from mywebnote.check_user import CheckUser
from mywebnote.add_user import AddUser

urlpatterns = [
    path('login/', mynote.login),
    path('registration/', mynote.registration),
    path('first/', mynote.first),   # start page
    path('feedback/', mynote.feedback),
    path('my-textarea/', my_textarea, name='my-textarea'),
    path('CheckUser/', CheckUser, name='CheckUser'),    # JSON login.html
    path('main/', mynote.main),
    path('AddUser/', AddUser, name='AddUser'),
]
