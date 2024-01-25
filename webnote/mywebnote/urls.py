from django.urls import path
import mywebnote.views as mynote
from mywebnote.pymain import my_feedback
from mywebnote.check_user import CheckUser
from mywebnote.add_user import AddUser

urlpatterns = [
    path('login/', mynote.login),
    path('registration/', mynote.registration),
    path('first/', mynote.first),   # start page
    path('feedback/', mynote.feedback),
    path('my_feedback/', my_feedback, name='my_feedback'),
    path('CheckUser/', CheckUser, name='CheckUser'),    # JSON login.html
    path('some_page/', mynote.some_page),
    path('AddUser/', AddUser, name='AddUser'),
]
