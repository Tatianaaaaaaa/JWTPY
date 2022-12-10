import jwt

payload_data = {
  "iat": 1670430472,
  "exp": 1671035272,
  "application_id": "3b7ce5ac-48b8-41f0-8e1f-5b0ca1e1cf61"
}



key = "-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCpYV20Ivl6WZsb
cxCIHzxQjyccclA0GnbLVnEtHwvuFe1CnLUMUOdsI5QRvMHct8Uai/htxQSBLOAj
018MG2k//QAjEM9QvlciQuUcLsZ0z+w4OjnGoLdvgu9ijZhuHxCutvD8qxyQZf89
2vfq27zAz+JUuk5WuwLJdX03H/LJR3j0bEbp0GuziQeXfMLllm0jXyLE/LeBDQq4
bf1N1cS47GyAer0F7u3KzjM6plqvW/mZUlrHkfjewtZB2PJiSOMSQGNZCDkwVICt
xRjr4GWotAvz5OXEx/KGTCG7PmAKaKP8KNZSZ2vrgU/xPOlChwcgzQuucDTuRy8t
B9dVzyf9AgMBAAECggEASZubDZv/X+jN661i+0zbuMSlQgr5iNMRWgdcUrgBxrs3
qvGQCmSkVY3WnKizdNhV61X1pbpvXTWjyF3kmc3VvO2VYCe/eH7nPeflSgyXyQ7M
wJipIAUbAnZb0q/nFMAiT1MIQj2YQbZZqEde4u0QR5hv6tM2FSHbMbKBsnGLYGWe
MG1ntarvdUgehX/i07cbj4mPphuU8uNZXWqdX5LebUh9g688eqNdhR3mMaqxC5KO
z48tvTUlDmhyd+iGWCvd17NdvfFnrZrr8pnvQk9oZQoKQm4U9UxHfqu2LZsrXOws
i0JUkokE+Zz7qr5Xa76qqrT2c8sNrTZkhvyREI2JvwKBgQDeJ6cztxtTyDgjKPvr
kwPVN6NN5LnPEfmHVpG8VtnQ5NRqD7K70E4FS8fhoNBxcnPTOy7emPqqYOvTlkZW
eyag/X5SmrrL2aXgsq0vxikKpUmPorkI4i+dEoaLrqWAQyFP4NTZtbZICvyyd60D
WEwcoBOT/B1R8HLQU+XwPEAFnwKBgQDDL26yn7Oxz6lujdMtpMrAdCJ9HmXD54sY
aTVvpTnkl2hv2SnoOzUWo60r5KPJ6QY0Ttld6fSAql1rDTvkxZBgnoiWmVJuw2Fk
89PBgWBEf1MRTtg/UOIUBABKxXHZsmJgJKHlo269wHS/axTVaBehzdrDsWS2G+jJ
NPonl45U4wKBgFnP0CHxMeQSOtfEFuyrF86YWrX/9TqIuseDMRHiTtbL3DAwvoJ9
eT1c4KcP+5URv0+zSoSFdjlxS4XT6AXIbdqCARLmKQSGrjAELE33H9qE7hNaptG3
l6Y5uhk4dwI+oXYIoCSP+OxxPK3uAg0rIkIkWSXns/bPbatZb8lKoltjAoGBAKcW
qNYC/wp9shaxFJIjW2orQQcJCacORTXNgvAjao70ynPNXSGv5b+OuIU1wrzrXeNT
iKLrz+KBdV1aQ+aQ9gqwTE9Xy4iEe5C3ZpRlk6qvsMXFUDvLmu31iuZ3ZgItwid5
1JpIMVoBMjBXk8sow+pA1kDmUEfRVpNAZdGU3URvAoGBAMgCdP+fXzxvXwXhE9DD
CrbRaW2ZWRQGwrQV/SxZLA72qYOU5o6NU6CpFFNh7pWBSITXTXVz6MIzs8SZ8TSN
ii1hYf0LBJ2TZxbisMowgmvn+R4WtkshCc3E9b7HDDQv4Q+q6zFGoFTmx7VuwB+3
EqAVQ6JYIBTpU2JNAHF8JB+9
-----END PRIVATE KEY-----"

def handle(data):
    data["token"]  = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='HS256'
)
    
    
    return data
