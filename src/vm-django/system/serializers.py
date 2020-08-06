from rest_framework import serializers
from .models import User, Group, Practical


class PracticalSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Practical class objects
    """

    class Meta:
        model = Practical
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Group class objects
    """

    class Meta:
        model = Group
        fields = ('id', 'name', 'practical')


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Profile class objects
    """

    class Meta:
        model = User
        fields = ('first_name', 'group')
