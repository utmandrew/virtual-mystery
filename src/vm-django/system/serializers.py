from rest_framework import serializers
from .models import Profile, Group, Practical


class CourseSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Course
        fields ={'id','name','instructor_name'}
        extra_kwargs={
            'instructor_name'
        }

class PracticalSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Practical class objects
    """
    class Meta:
        model = Practical
        fields = ('id','name','ta_name')


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
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password','group',)
        extra_kwargs = {'password': {'write_only': True}}
