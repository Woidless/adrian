from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from . import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class OrderViewSet(APIView):
    permission_classes=(permissions.AllowAny,permissions.IsAuthenticated)

    def post(self, request, *args, **kwargs):
        serializer = serializers.OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fio = serializer.validated_data['fio']
        email = serializer.validated_data['email']
        number = serializer.validated_data['numer']
        address = serializer.validated_data['address']
        model = Order(fio=fio, email=email, number=number, address=address)
        model.save()
        return Response('Заявка отпралена', status=200)