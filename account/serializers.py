from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import CustomUser

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField( min_length=8, max_length=20,
                                      required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Passwords did not match')
        if not attrs['password'].isalnum():
            raise serializers.ValidationError('Password field must contain alpha symbols and numbers')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
