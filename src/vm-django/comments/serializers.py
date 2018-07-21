from rest_framework import serializers
from .models import Comment, Reply


class ReplyViewSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Reply class objects.
    """
    username = serializers.CharField(source='owner.username')

    class Meta:
        model = Reply
        fields = ('id', 'username', 'text')


class CommentViewSerializer(serializers.ModelSerializer):
    """
    Serializes Comment class objects.

    Note:
        - Used for sending specific comment object data at api endpoints

    """
    reply = ReplyViewSerializer(many=True, read_only=True)
    username = serializers.CharField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'username', 'text', 'reply')


class CommentCreateSerializer(serializers.ModelSerializer):
    """
    Deserializes and creates comment class objects from json data.

    Note:
        - Used for creating comment objects from specific data received through
          api endpoint post requests.

        - Add support for release (clue)

    """

    class Meta:
        model = Comment
        fields = ('owner', 'instance', 'text')
