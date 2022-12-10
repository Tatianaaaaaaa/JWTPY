import jwt

payload_data = {
  "iat": 1670696872,
  "exp": 1670700472,
  "application_id": "3b7ce5ac-48b8-41f0-8e1f-5b0ca1e1cf61"
}

key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC2kyeB8VtbEGQ5
mNjQ2OyKTeSvzazMtkGq5ta+g+rLxnLXa5wwoPXcM4jC1o6zJl9SskPFKfsfr8z3
42gBSwVbms4pfI+DPCU102O0KR5zS08rYSQzC5e7BTX+78MBV9OSL4sH23dN1txv
bOdXAIWqyYreUdqpHGfbebKtp5YpTdogBXbV6ODUUefSAAAX3wI3Wt4irCGYCMra
6lhekDzZ6ZGFdLyeBudpF/vwct5iCQoCpsefckMAWN9qPy7CSD2Q4d9xlvoa8H5j
PXH7uze6Y7vSNT4L4S2tZrUjx7xQibb3t0z/00joUqvyXwupJfeupOaQSIIgFSVx
PexVJV+VAgMBAAECggEAFI/sMilRpabp8saxHIxhz43IRLiATqn0KWBILTrENeEK
zBI1jBCEwCEZtP/fIHQg5jpngYwh2Ua+aei1rPebCd8cevWpYBllA3PkVcUPxeJk
bzlIj2st0oVauHSeXMdcb6llGiRwglbBitcUEutfIoYCWtmTK9qkI8bIBeDK+6m1
PPGCiBVdLHkBL7qUdRfhxRKa5skmNUs/J3jqrnPVIsBSt/0ENiJJV9pXYcZCZ+Dn
Eb1xPndLD3hq1sSzSe1msuo/iYPsrtD7kWiw7MHXMxjNpzcD6T3uMu7YKW/Rxe6h
PsOUCOH/T5N1tibgcmC6pX9HOzkivZvlsSzMMgrzXQKBgQDgeOpgRa8leZGcFY5W
f3JNQOT7RvP5O9U8iwyan8IczJC8RrFs+0yeDb5cd/Bhj8pcugplJw26GONprqPt
BfFFiyWAebOvu0GVC8/f2B20qiVvSoc7szkA2nkmHsRqAPPynzkt4vSWUrB/khWt
X/Vg0bSqISPmqrTwg1XdoshfLwKBgQDQN8exMnqvdrMyfuN83WYNaFk9Ba9QRALY
Mqj7ZmnVmczDnXVet8NtLiIwuMp8Da6Rce+gPrrYGFighqkX9G8WQW2fl5cMirPb
oL2BTVArPyKzDeHbWlynS/ANd2Z5i/SNHZsfwXo2XMuBm3ifEO1Ee0WaGOgex5av
L8nVyVGcewKBgEyr4FpL0vw43uxyTHDtDSyn+s59OL4rmrUYRZDW+qV9lf5JIzc3
Sr89sITDDt80DwnHHd/ZDA5BjAO//AvsmLGJSqDscNyYWFlBdJpfph3cc/bkfPZ+
S/0nonPL1IjklG6NxikPOT3TNqgMTM0wVo7gchYeRbX3HuB766tNe6VPAoGBAKDy
HPeJT3AFzqo/jtRbxqCigig7FrJyf8hiEGCTX0dupOqn8auPXA4u1NrYXBvb744Z
heJV2tNirk8XB+muVZfcZ0IvSOC27iPccd9axZdILCg/mM+XX3sppZqjKqDVX+kc
c2Xuhesze1LpvCkoSl7e8oQUsIfqOz2bMOaBwQW1AoGBALJm7yKF9NcjwBEEoqG9
pSSqmLVQJQKqz0OnuhrHflVUfNT/aBUAhjCfWO/Vf/5w4xtvDIpN3ZxXqKxP5Nii
ZWr26Y13WxGvf2+A/FGq/VmKji5xQo87VjScZmHphKmXjyXxyDCDSdn6mbV8t1v6
Wzwnfk58/ZUPixxmnTeMDBoJ
-----END PRIVATE KEY-----
"""

def handle(data):
    data["token"]  = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='HS256'
)
    
    
    return data
