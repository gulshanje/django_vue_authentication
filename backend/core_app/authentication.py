import jwt
from datetime import datetime, timezone, timedelta

def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp' : datetime.now(timezone.utc) + timedelta(minutes=15),
        'iat' : datetime.now(timezone.utc),
    }, 'access_secret', algorithm='HS256')

def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp' : datetime.now(timezone.utc) + timedelta(days=7),
        'iat' : datetime.now(timezone.utc), 
    }, 'refresh_secret', algorithm='HS256')