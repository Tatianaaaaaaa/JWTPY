import jwt

payload_data = {
  "iat": 1670430472,
  "exp": 1671035272,
  "application_id": "3b7ce5ac-48b8-41f0-8e1f-5b0ca1e1cf61"
}



key = 'my_super_secret'

def handle(data):
    data["token"]  = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='HS256'
)
    
    
    return data
