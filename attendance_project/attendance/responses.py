import uuid
import datetime

def create_register_response(rrid,deviceserialno):
    register_response = f"""
<?xml version="1.0"?>
<Message>
<Response>Register</Response>
<Actid>{rrid}</Actid>
<Time>{datetime.datetime.now().isoformat()[:-7] + 'Z'}</Time>
<DeviceSerialNo>{deviceserialno}</DeviceSerialNo>
<Token>{uuid.uuid4()}</Token>
<Result>OK</Result>
</Message>
"""
    print(register_response)
    return register_response

def create_login_response(rrid, deviceserialno):
    login_response = f"""
    
<?xml version="1.0"?>
<Message>
<Response>Login</Response>
<Actid>{rrid}</Actid>
<Time>{datetime.datetime.now().isoformat()[:-7] + 'Z'}</Time>
<DeviceSerialNo>{deviceserialno}</DeviceSerialNo>
<Result>OK</Result>
</Message>
"""
    print(login_response)
    return login_response
