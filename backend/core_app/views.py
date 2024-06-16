from django.shortcuts import render
from core_app.authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from core_app.models import User, UserToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import exceptions
from .serializers import UserSerializer
from datetime import datetime, timezone, timedelta
# Create your views here.

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password do not match')
        
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid credentials')
        
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials')
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        UserToken.objects.create(user_id= user.id, token = refresh_token, expired_at =  datetime.now(timezone.utc) + timedelta(days=7), )
        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'token' : access_token
        }
        
        return response
        # serializer = UserSerializer(user)
        # return Response(serializer.data)

class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        return Response(UserSerializer(request.user).data)
    
class RefreshTokenAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter( user_id = id, token=refresh_token, expired_at__gt=datetime.now(timezone.utc)).exists():
            raise exceptions.AuthenticationFailed('Unauthenticated')
        
        access_token = create_access_token(id)
        return Response({'token':refresh_token})

class LogoutAPIView(APIView):
    # authentication_classes = [JWTAuthentication]

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        UserToken.objects.filter(token=refresh_token).delete()
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'Successfully logout'
        }
        return response