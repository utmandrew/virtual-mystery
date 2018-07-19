from rest_framework import serializers
from .models import Comment, Reply


class ReplySerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Reply class objects.
    """
    username = serializers.CharField(source='owner.username')

    class Meta:
        model = Reply
        fields = ('id', 'username', 'text')


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Comment class objects.

    Note:
        - Do not need to include instance

    """
    reply = ReplySerializer(many=True, read_only=True)
    username = serializers.CharField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'username', 'instance', 'text', 'reply')
