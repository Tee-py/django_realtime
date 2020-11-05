import json
from channels.generic.websocket import WebsocketConsumer
from .views import *
import asyncio

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        while True:
            asyncio.sleep(10)
            self.send(text_data=json.dumps({
                'message': NotificationSerializer(Notification.objects.all(), many=True).data
            }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': NotificationSerializer(Notification.objects.all(), many=True).data
        }))