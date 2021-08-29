from chat.models import Chat
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async, async_to_sync


"""MESSAGE DB ENTRY"""
@sync_to_async
def create_new_message(me,message):
    author_user = User.objects.filter(username=me)[0]
    new_chat = Chat.objects.create(
        author=author_user,
        text=message)
        

class ChatRoomConsumer(AsyncWebsocketConsumer):
    
    """Connect"""
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']
        self.room_group_name = 'chat_room'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    """Disconnect"""
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    """Receive"""
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await create_new_message(me=username, message=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )


    """Messages"""
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
