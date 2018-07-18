from rest_framework import serializers
from .models import Mystery, Instance


class MysterySerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Mystery class objects
    """
    class Meta:
        model = Mystery
        fields = ('id', 'name')


class InstanceSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Mystery class objects
    """
    class Meta:
        model = Instance
        fields = ('id', 'group', 'mystery')
