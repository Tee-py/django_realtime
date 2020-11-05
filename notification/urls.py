
from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("nots", get_notifications, name="nots")
]
