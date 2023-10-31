from django.urls import path
import dzsite.views as views

urlpatterns = [
    path('<slug:npage>', views.pages),  # http://127.0.0.1:8000/dzsite/{npage}
]
