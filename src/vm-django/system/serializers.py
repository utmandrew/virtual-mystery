from rest_framework import serializers
from .models import Profile, Group, Practical


class PracticalSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Practical class objects
    """
    class Meta:
        model = Practical
        fields = ('id',)

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
        model = Profile
        fields = ('group',)
