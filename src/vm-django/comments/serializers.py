from rest_framework import serializers
from .models import Comment, Reply


class ReplyViewSerializer(serializers.ModelSerializer):
    """
    Serializes Reply class objects.

    Note:
        - Used for sending specific reply object data at api endpoints.

    """
    username = serializers.CharField(source='owner.username')

    class Meta:
        model = Reply
        fields = ('id', 'username', 'text')


class ReplyCreateSerializer(serializers.ModelSerializer):
    """
    Deserializes and creates reply class objects from json data.

    Note:
        - Used for creating reply objects from specific data received through
          api endpoint post requests.
    """

    class Meta:
        model = Reply
        fields = ('owner', 'text', 'parent')


class CommentViewSerializer(serializers.ModelSerializer):
    """
    Serializes Comment class objects.

    Note:
        - Used for sending specific comment object data at api endpoints.

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
    """

    class Meta:
        model = Comment
        fields = ('owner', 'instance', 'release', 'text')
