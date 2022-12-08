import jwt


def handle(data): {
    'sub': '4242',
    'name': 'Jessica Temporal',
    'nickname': 'Jess'
}

secret = 'my_super_secret'
token = jwt.encode(payload=payload_data, key=secret)
return data
