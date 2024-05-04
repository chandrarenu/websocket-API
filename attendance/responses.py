import uuid
import datetime

def create_register_response(rrid,deviceserialno):
    token = str(uuid.uuid4())
    timestamp = datetime.datetime.now().isoformat()[:-7] + 'Z'
    register_response = f"""<?xml version="1.0"?>

<Message>
    <Response>Register</Response>
    <Actid>{rrid}</Actid>
    <Time>{datetime.datetime.now().isoformat()[:-7] + 'Z'}</Time>
    <DeviceSerialNo>{deviceserialno}</DeviceSerialNo>
    <Token>{token}</Token>
    <Result>OK</Result>
</Message>"""

    # print(register_response)
    return register_response

def create_login_response(rrid, deviceserialno, token=None):
    if not token:
        token = str(uuid.uuid4()) 
        
    timestamp = datetime.datetime.now().isoformat()[:-7] + 'Z'
    
    login_response = f"""<?xml version="1.0"?>
    
<Message>
    <Response>Login</Response>
    <Actid>{rrid}</Actid>
    <Time>{datetime.datetime.now().isoformat()[:-7] + 'Z'}</Time>
    <DeviceSerialNo>{deviceserialno}</DeviceSerialNo>
    <Token>{token}</Token>
    <Result>OK</Result>
</Message>"""


    # print(login_response)
    return login_response

def create_time_log_response(rrid, deviceserialno):
    timestamp = datetime.datetime.now().isoformat()[:-7] + 'Z'
    
    time_log_response = f""" <?xml version="1.0"?>
    
<Message>
    <Response>TimeLog</Response>
    <Actid>{rrid}</Actid>
    <Time>{datetime.datetime.now().isoformat()[:-7] + 'Z'}</Time>
    <Result>OK/Fail</Result>
</Message>"""
    
    
    # print(time_log_response)
    return(time_log_response)
