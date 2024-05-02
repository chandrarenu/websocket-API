from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AttendanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        print("-----------------------------")
        # self.scope['session'].id
        
    
        await self.accept()
        
        print("connection established")


    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        print(text_data)
        # attendance_data = json.loads(text_data)
        
    