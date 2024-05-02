from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AttendanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        attendance_data = json.loads(text_data)
        