from django.urls import path
import mywebnote.views as mynote
from mywebnote.pymain import feed_back
from mywebnote.check_user import CheckUser
from mywebnote.add_user import AddUser
from mywebnote.recover_user import RecoverUser

urlpatterns = [
    path('login/', mynote.login),
    path('registration/', mynote.registration),
    path('first/', mynote.first),   # start page
    path('feedback/', mynote.feedback),
    path('feed_back/', feed_back, name='feed_back'),
    path('CheckUser/', CheckUser, name='CheckUser'),    # JSON login.html
    path('some_page/', mynote.some_page),
    path('AddUser/', AddUser, name='AddUser'),
    path('dish_order/', mynote.dish_order),
    path('recover/', mynote.recover),
    path('RecoverUser/', RecoverUser, name='RecoverUser'),
]
