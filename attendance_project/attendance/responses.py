import datetime
import uuid
def create_register_response(rrid,serial):
    register_response = f"""
<?xml version="1.0"?>
<Message>
<Response>Register</Response>
<Actid>{rrid}</Actid>
<Time>{datetime.datetime.now().isoformat()[:-7] + 'Z'}</Time>
<DeviceSerialNo>{serial}</DeviceSerialNo>
<Token>{uuid.uuid4()}</Token>
<Result>OK</Result>
</Message>
"""
    print(register_response)
    return register_response