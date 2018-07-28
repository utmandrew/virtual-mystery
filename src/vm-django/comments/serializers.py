from rest_framework import serializers
from .models import Comment, Reply


class ReplySerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes and creates reply class objects.
    """
    username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Reply
        fields = ('id', 'username', 'owner', 'text', 'parent')
        read_only_fields = ('id', 'username')
        extra_kwargs = {'owner': {'write_only': True},
                        'parent': {'write_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Comment class objects.
    """
    reply = ReplySerializer(many=True, read_only=True)
    username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'username', 'text', 'reply', 'owner', 'instance',
                  'release')
        read_only_fields = ('id', 'username', 'reply')
        extra_kwargs = {'owner': {'write_only': True},
                        'release': {'write_only': True},
                        'instance': {'write_only': True}}


# class CommentViewSerializer(serializers.ModelSerializer):
#     """
#     Serializes Comment class objects.
#
#     Note:
#         - Used for sending specific comment object data at api endpoints.
#
#     """
#     reply = ReplyViewSerializer(many=True, read_only=True)
#     username = serializers.CharField(source='owner.username')
#
#     class Meta:
#         model = Comment
#         fields = ('id', 'username', 'text', 'reply')
#
#
# class CommentCreateSerializer(serializers.ModelSerializer):
#     """
#     Deserializes and creates comment class objects from json data.
#
#     Note:
#         - Used for creating comment objects from specific data received through
#           api endpoint post requests.
#     """
#
#     class Meta:
#         model = Comment
#         fields = ('owner', 'instance', 'release', 'text')
