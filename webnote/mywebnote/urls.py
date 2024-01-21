from django.urls import path
import mywebnote.views as mynote
from mywebnote.pymain import my_logreg, my_textarea
from mywebnote.check_user import CheckUser

urlpatterns = [
    path('login/', mynote.login),
    path('registration/', mynote.registration),
    path('first/', mynote.first),   # start page
    path('feedback/', mynote.feedback),
    # path('my-logreg/', my_logreg, name='my-logreg'),
    path('my-textarea/', my_textarea, name='my-textarea'),
    path('CheckUser/', CheckUser, name='CheckUser'),
    path('main/', mynote.main),
]
