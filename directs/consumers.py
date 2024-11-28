import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('call_group', self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('call_group', self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        await self.channel_layer.group_send(
            'call_group', 
            {
                'type': 'relay_message',
                'message': data,
                'sender_channel': self.channel_name
            }
        )

    async def relay_message(self, event):
        # Only send to other channels
        if event['sender_channel'] != self.channel_name:
            await self.send(text_data=json.dumps(event['message']))