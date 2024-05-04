from channels.generic.websocket import AsyncWebsocketConsumer
import xml.etree.ElementTree as ET
from attendance.responses import create_register_response, create_login_response, create_time_log_response


class AttendanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("WebSocket connection established")

    async def disconnect(self, close_code):
        print(f"WebSocket connection disconnected with close code {close_code}")
        

    async def receive(self, text_data):
        try:
            print("Received message:")
            print(text_data)
            print("-------------------------------------------------------------------------")
            
            tree = ET.fromstring(text_data)
            print("Parsed XML tree:")
            ET.dump(tree)
            
            request_element = tree.find('Request')
            
            if request_element is None or request_element.text is None:
                raise ValueError("'Request' element not found in XML message.")
                # print("Error:'Request' element not found in XML message.")
                # return
            
        # request_type = tree.find('Request').text
            request_type = request_element.text.strip()
            print(f"Request Type: {request_type}")
        
            if request_type == "Register":
                
                rrid_element = tree.find('Rrid')
                productname_element = tree.find('ProductName')
                deviceserialno_element = tree.find('DeviceSerialNo')
                
                if None in (rrid_element, productname_element, deviceserialno_element):
                    raise ValueError ("Required data for 'Register' request is missing.")
                    # print("Error: Required data for 'Register' request is missing.")
                    # return
                
                rrid = rrid_element.text.strip() if rrid_element is not None else None
                productname = productname_element.text.strip() if productname_element is not None else None
                deviceserialno = deviceserialno_element.text.strip() if deviceserialno_element is not None else None

                
                if None in (rrid, productname, deviceserialno):
                    raise ValueError("Required data for 'Register' request is missing or invalid.")
            

                
                
                response = create_register_response(rrid, deviceserialno)
                await self.send_response(response)
                

                
            elif request_type == "Login":
                rrid_element = tree.find('Rrid')
                deviceserialno_element = tree.find('DeviceSerialNo')
                token_element = tree.find('Token')
                
                if None in (rrid_element, deviceserialno_element):
                    raise ValueError ("Required elements for 'Login' request are missing.")
                    # print("Error: Required elements for 'Login' request are missing.")
                    # return
                
                rrid = rrid_element.text.strip() if rrid_element is not None else None
                deviceserialno = deviceserialno_element.text.strip() if deviceserialno_element is not None else None
                token = token_element.text.strip() if token_element is not None and token_element.text else None
                
                if None in (rrid, deviceserialno):
                    raise ValueError("Required data for 'Login' request is missing or invalid.")
                
                
                    
                    
                response = create_login_response(rrid, deviceserialno, token)
                await self.send_response(response)
                
            elif request_type == "TimeLog":
                rrid_element = tree.find('Rrid')
                deviceserialno_element = tree.find('DeviceSerialNo')
                # productname_element = tree.find('ProductName')
                if None in (rrid_element, deviceserialno_element):
                    raise ValueError ("Required data for 'TimeLog' request is missing.")
                    # print("Error: Required data for 'TimeLog' request is missing.")
                    # return
                
                rrid = rrid_element.text.strip() if rrid_element is not None else None
                deviceserialno = deviceserialno_element.text.strip() if deviceserialno_element is not None else None
                
                if None in (rrid, deviceserialno):
                    raise ValueError("Required data for 'TimeLog' request is missing or invalid.")
                
                
                response = create_time_log_response(rrid, deviceserialno)
                await self.send_response(response)
                
        except Exception as e:
            print(f"Error processing request: {e}")
                
            
            
            
        
            
    async def send_response(self, response):
        try:
            await self.send(text_data=response)
        except Exception as e:
            print(f"Error sending response: {e}")