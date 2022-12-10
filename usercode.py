import jwt

payload_data = {
  "iat": 1670430472,
  "exp": 1671035272,
  "application_id": "3b7ce5ac-48b8-41f0-8e1f-5b0ca1e1cf61"
}

key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqWFdtCL5elmbG3MQiB88
UI8nHHJQNBp2y1ZxLR8L7hXtQpy1DFDnbCOUEbzB3LfFGov4bcUEgSzgI9NfDBtp
P/0AIxDPUL5XIkLlHC7GdM/sODo5xqC3b4LvYo2Ybh8Qrrbw/KsckGX/Pdr36tu8
wM/iVLpOVrsCyXV9Nx/yyUd49GxG6dBrs4kHl3zC5ZZtI18ixPy3gQ0KuG39TdXE
uOxsgHq9Be7tys4zOqZar1v5mVJax5H43sLWQdjyYkjjEkBjWQg5MFSArcUY6+Bl
qLQL8+TlxMfyhkwhuz5gCmij/CjWUmdr64FP8TzpQocHIM0LrnA07kcvLQfXVc8n
/QIDAQAB
-----END PUBLIC KEY-----"""

def handle(data):
    data["token"]  = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='HS256'
)
    
    
    return data
