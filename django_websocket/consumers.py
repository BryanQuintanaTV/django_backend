import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    clients = set()

    def connect(self):
        self.accept()
        ChatConsumer.clients.add(self)

    def disconnect(self, close_code):
        ChatConsumer.clients.remove(self)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        for client in ChatConsumer.clients:
            client.send(text_data=json.dumps({'message': message}))
