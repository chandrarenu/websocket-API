from channels.generic.websocket import AsyncWebsocketConsumer
import xml.etree.ElementTree as ET
from attendance.responses import create_register_response

class AttendanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("connection established")

    async def disconnect(self, close_code):
        print(f"connection disconnected with close code {close_code}")
        pass

    async def receive(self, text_data):
        print(text_data)
        print("-------------------------------------------------------------------------")
        tree = ET.fromstring(text_data)
        request_type = tree.find('Request').text
        
        if request_type == "Register":
            rrid = tree.find('Rrid').text
            print(rrid)
            productname = tree.find('ProductName').text
            print(productname)
            deviceserialno = tree.find('DeviceSerialNo').text
            print(deviceserialno)

            self.send(create_register_response(rrid,deviceserialno))
        if request_type == "Login":
            token = tree.find("Token")

            
            
            
        
        # attendance_data = json.loads(text_data)
        
    