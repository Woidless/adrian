from rest_framework import serializers
from .models import Person


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')
        