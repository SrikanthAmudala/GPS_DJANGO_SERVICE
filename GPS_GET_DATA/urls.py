from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getgpsdata/', views.get_data_gps),
]