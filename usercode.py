import jwt
import calendar
import datetime
from datetime import timedelta 

date1 = datetime.datetime.utcnow() 
date2 = datetime.datetime.utcnow() + timedelta(days=6)

payload_data = {
  "iat": calendar.timegm(date1.utctimetuple()),
  "exp": calendar.timegm(date2.utctimetuple()),
  "application_id": "7bcd9724-cc29-4541-9863-94d26ac58cb3"
}

key = "-----BEGIN PRIVATE KEY-----MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDX2gi+iBgbRHA0NTk4LqbcuP5h1IOJTTJGFZoRqucAAKwehoKPaQEtVUJ1QIy5VORV7MSJs/3EQxPCEvbjMpplNaorFWOp6drBVzn+jvccXMYPNjs7Sx39yvV+U1WykXqvWnXGIOGZDay7oJdruy6CL6xCieHo34T/d+io17/5OgBvXzLH05zUw+JpM5zgbU+t2jH3nHB4EzBEWQlTw7BBQV7YChm/zYGH+LQdrBmPzFsc+x0CU96Ff0wjT8xW/9bs7Qf0iDmCc1Vxx3JHNwWRWi96PlpBuBuvIOBkeF0uAN+HPDzvCuUT/Pao/3cNzaONDULAZZfDr7dQax92Aql1AgMBAAECggEAGPk+gsDfPSRlcPzpcmEfaDE1KV97moKmeupb6Yhi8qKhR2TbrTkCbFrNdiByR60VQAXFVYNQLIlwO0eTbgT4TRZw6kwuvEV0zGLJsHSdDZiER9VH9BvETA1T6vo8U402axxlvPcn8tvcrNavPkUpY+GdJhOq4hUeX6phbkuMCAsh6ebbJmue+XFGqA160awMGhFFSLY14mDF0GxsoWKAoLyj/qq7C2DbZWX+hX/d9Q8IrXJ4I6Bu+ydlgN7hPRfFod4QK2H6dkY34i6oRHgwIKjd277q4guTD4ddkJ3WYHjGw26FZTScl/vEwUHI4WxyffquEJJPDRsDfYDDp+xnzwKBgQD6XrvHfPzK+YDOePbXj/0DvM0oPXblNUc1hec8y+X/R+bv+a1f5rcbHrmGOKq72OK/SHJ8gg5hzLy03CtaVABRnloYkP40exP3IzrA6TtS4sPzAoiIod2EhGIrfUZvxtb7CkR0ldu7tjbJY2RnzE4zXcDppHkE+hBO4LX9TqghwKBgQDctJgba0rHWrjJHGBk2eerbvQcHHHcETH3xCi8e72vPn0ZSd6Z3ysAoIkjNYgG7pHE3lYqs859U5RmNnfIdcnU5WHLGLe4wIRZaipc4Toj/kSHw8kSQlIeSsjYMdTiFkh6s9Rk1l/oTtMnt7CwVZll7EPZVXjCi3dKTwltnSxRIwKBgQDd/D6r+kK8yImPB6t8pvrjZHPWOOEBCsMPTqEew34yYJL+tLYm8I3q6sv9mKKwmPU6Okbf5ARSbE/oX8nEdfQuaaNiYrQw3etu1PqT8OGhv7gVkohtiYXnhs+rCunlIQ9l6jbjyUaiYf0+GMazlZzzyyC5yOdTfN8Rb21sgs6vYwKBgAuDlGfhyg3qard7NoAsagykhjGtPjdn4j51ylZC8lthHC+kjetjHCA1P9JJaaZK7eniW4ZwyPX61UQb1VXs5zGnIdnxmSwXRxBPHJSp31mfWz3l9ehw803HQwEcYGnHFdLo7Myx7mD1M8jfqWUZoh4SHFwLPHiRxBBpXSmNyJEXAoGADJGxo0FyzokpM4MIGv6uKi13tG0USUnQEFKPlDgglunVky+7OyKns6XRx4A8EFeGl7VxMjhfuw5DeJAVSxNEkC3DNUMLGYvTZTXA45/yzf0mEET7f7ArGykHq6BBCdw0f1JNGAUBdPo5PDPL3MQWlsnKyK9rtSxRNIrp6v6F6Uo=-----END PRIVATE KEY-----"


def handle(data):

  
    data["token"]  = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='HS256'
)
    
    
    return data
