# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
# my apps
from . import serializers
from .send_email import send_confirmation_email
# django
from django.contrib.auth import get_user_model, authenticate, logout, login


# 6
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

# 
User = get_user_model()


class RegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            if user:
                send_confirmation_email(user=user.email, code=user.activation_code)
            return Response('check email', status=201)
        return Response('Bad request', status=400)
    

class ActivationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Successfully activated!'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Link expired!'}, status=400)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        email = serializer.validated_data['email']
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'Token': token.key}, status=200)
        else: return Response({'message': 'Неверные учетные данные'}, status=400)
        

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        logout(request)
        return Response({'message': 'Выход выполнен успешно'}, status=200)
    