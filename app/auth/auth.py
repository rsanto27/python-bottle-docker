import jwt
import datetime
import time

import settings as sett

settings = sett.Settings()

def get_token(user):
    key = settings.key
    return jwt.encode(user, key, algorithm='HS256').decode("utf-8")

def decode_token(token):
    key = settings.key
    return jwt.decode(token, key, algorithms=['HS256'])

def verify_token(token):
    decoded = decode_token(token)

# settings = Settings()
# key = settings.key

# encoded = jwt.encode({'some': 'payload'}, key, algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})
# print(encoded)
# print(key)

# decoded = jwt.decode(encoded, key, algorithms=['HS256'])
# print(decoded)

# ##########################################################
# a = datetime.datetime.utcnow()
# b = datetime.timedelta(seconds=30)
# print(a)
# print(b)
# jwt_payload = jwt.encode({
#     'exp': a + b,
#     'some': 'payload'
# }, 'secret')

# time.sleep(32)

# JWT payload is now expired
# But with some leeway, it will still validate

# decoded = jwt.decode(jwt_payload, 'secret', leeway=10)
# print(decoded)
# #########################################################

# foo = Settings()
# bar = Settings()
# print(foo is bar)
# print(foo.key)
# print(bar.key)