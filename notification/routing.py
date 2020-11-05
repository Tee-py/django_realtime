#from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from .consumers import *

socket_urlpatterns = [
    #path('/ws/', ChatConsumer.as_asgi()),
    re_path(r'/$', NotificationConsumer.as_asgi()),
]




