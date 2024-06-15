from core_app.serializers import UserSerializer
import jwt, datetime
from datetime import datetime, timezone, timedelta
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from .models import User

# Create middleware
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            user = User.objects.get(pk=id)
            return (user, None)
        raise exceptions.AuthenticationFailed('unauthenticated')

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

# Decode access token
def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
    

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')