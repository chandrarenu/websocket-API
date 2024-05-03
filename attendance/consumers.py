from channels.generic.websocket import AsyncWebsocketConsumer
import xml.etree.ElementTree as ET
from attendance.responses import create_register_response, create_login_response, create_time_log_response


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
            productname = tree.find('ProductName').text
            deviceserialno = tree.find('DeviceSerialNo').text
            
            response = create_register_response(rrid, deviceserialno)
            await self.send_response(response)
            

            
        elif request_type == "Login":
            rrid = tree.find('Rrid').text
            deviceserialno = tree.find('DeviceSerialNo').text
            token = tree.find('Token').text if tree.find('Token') is not None else None
            response = create_login_response(rrid, deviceserialno)
            await self.send_response(response)
            
        elif request_type == "TimeLog":
            rrid = tree.find('Rrid').text
            deviceserialno = tree.find('DeviceSerialNo').text
            productname = tree.find('ProductName').text
            
            response = create_time_log_response(rrid)
            await self.send_response(response)
            
            
            
            
        
            
    async def send_response(self, response):
        await self.send(response)