from django.urls import path
import dz47url.views as dz47url

urlpatterns = [
    path('', dz47url.index_dz_url),
]
