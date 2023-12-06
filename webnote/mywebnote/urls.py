from django.urls import path
import mywebnote.views as mynote
from mywebnote.pymain import my_logreg, my_textarea

urlpatterns = [
    path('login/', mynote.login),
    path('registration/', mynote.registration),
    path('my-logreg/', my_logreg, name='my-logreg'),
    path('first/', mynote.first),   # start page
    path('feedback/', mynote.feedback),
    path('my-textarea/', my_textarea, name='my-textarea'),
]
