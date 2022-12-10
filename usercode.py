import jwt

payload_data = {
  "iat": 1670430472,
  "exp": 1671035272,
  "jti": "8TSuQqpkpAQC",
  "application_id": "3b7ce5ac-48b8-41f0-8e1f-5b0ca1e1cf61"
}



key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC3w4/J/kNHI8Rd
54CjMsLyMQlxph7e7MmA1xulO7sza5zxHuLobk6R2HssVChAj5948DiktUqEsC+h
SPPU8rq1Nh8GG7hO8ZW9ZOMgYFkf302RCcxuvgxxKCpdnw/tLtOJyGjGL7TEvK7i
/F2ki2rtNZMuKCrG7uzzZtEPzoNt9IhhMmpbzi01Yvhn6YZwC6nlhFUneI7fbkjC
4kCKyxjwPoMJLSmG5w6Md0EAxeaERPzQ/SGhLfbfNOfRTU7LfBJjFaEUiy+mVkMC
0yc3bfOecKXztTIybsjyE96YTL7xAHsKEoclMhSEl3Pesrzb8+zWCDV8yZWQ2nBm
bVPM84/HAgMBAAECggEAHR/2oyoUWasWjVeKsNLzyNTyzTtp+yUGTtBJBmgwJFcy
+ZhOmE4bT8xCwWTZOFpLCSzxnVFKbTtLYUGhu6d45g2c3yf3jzOE6w6ZXOFIXt/S
eGFYMFkYubqG9G2oZYwdZOIJkRewi9nn0fvzj4e1O8FZAWDGXt8xWOZ7zgiKFhv9
24v5uzw99l3IEIKbJYFqqyHifN6IbysJMixaPPYuQ4S/mqt1bR80bItkahiF8xEG
oC/00y2tWUMypNZ0xKS2sh0qrgVft8/st7AHBeY+RARJo4V6mPUXezRYFRSzRgsR
J4AB/sj08DeAcmz8clBvUSZ5sxSZQRWR9gI2qwzhkQKBgQDbfjdLYUKqxhWMTq9G
Lfr0G7q0rXj5HlZ2Wg6bEaBWtE4708c/5ZMYMgd3xW7KNbTo3BN5LVSOKWq2nj/i
vvBrYumbbo+FCrIiTeL50x0h/wxhRh4MfvjFYlwok1sKPr/6Rd7alBNOHq+TNBYv
mMR64v99K2488M1maqITc9zxqQKBgQDWVAmB7Y6cLNA1gAKiDSkhVKe/aeEXFIiR
u5M8WXyBLPQSFfKwdhuO8auUKBGIg4cwMis3cki/XhweUc70JJBNV5Iclt+mcCyO
V7U7EoIoDOfc3379ttIOfzvOup3Zy44iNas+xfAtBUHYMKB5RFi8kEgpudMeUfOU
D9oFu5w77wKBgHt58ZlSSbLQZGbeDPQqAbc5sjraK+fZDULfPsA1lkGwhSJa7Qgh
GjLOUi0qwDy5IeCtjbbprVucKRA6zi28xHtk1Y4/EDYD4lox/rIT9ZueY1SFoXne
JAzGXJnm65xD2LPugoPsMUANOzBQaPq1sjJ/aML9n7JgtOwcqLjQwUahAoGBALzb
3mjcAL9DidCq1Scgu66AHzS/QrYIxPLNu8cA/4IAL63EI081M8F42P07dX+6jqR8
gLJiBRKEBfj9k4R0t6c/VCPXGopZ7Bkd1jeQbpqGDMYHNqqwr1ZQ7U2UCcZB5SPl
8NjmqGWzbTroVm+lNyApbz09XngoNJ+yfCZzFA+HAoGBAIGAddNiBOHu5WcNkM3D
udwtoUmYxCE6HC6OjADBWFt2Rl2MJjur3GayH/HUQE2/8kEdxkBcxYaPLZAU5GkK
+JjtMgJGrG3UpLjuE+FVe8QF9HtGOuAfpSBcy9i7vMOgz4NCioB0bJMwOk5xte6G
qdWqgOpO1rrya2mIsRKcbGyP
-----END PRIVATE KEY-----
"""

def handle(data):
    data["hello"] = "Hello world!"
    token = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='HS256'
)
    
    
    return data
