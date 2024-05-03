import uuid
import datetime

def create_register_response(rrid,deviceserialno):
    token = str(uuid.uuid4())
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

def create_login_response(rrid, deviceserialno, token=None):
    if not token:
        token = str(uuid.uuid4()) 
    
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

# def create_time_log(act_id, result):
#     time_log_responses = f"""
    
#     <?xml version="1.0"?>
#     <message>
#     <Response>TimeLog</Response>
#     <Actid>{rrid}</Actid>
#     <Time>{datetime.datetime.now().isoformat()[:-7] + 'Z'}</Time>
#     <Result>OK/Fail<Result>
#     </Message>
#     """