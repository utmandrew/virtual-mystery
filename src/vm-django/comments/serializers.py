from rest_framework import serializers
from .models import Comment, Reply, Result


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


class ResultSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Result class objects
    """

    class Meta:
        model = Result
        fields = ('owner', 'mark', 'feedback', 'comment', 'id')
        #extra_kwargs = {'owner': {'write_only': True},
                        #'feedback': {'write_only': True},
                        #'mark': {'write_only': True},
                        #'comment':{'write_only':True}}


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes/Deserializes Comment class objects.
    """
    reply = ReplySerializer(many=True, read_only=True)
    result = ResultSerializer(many=True, read_only=True)
    username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'username', 'text', 'marked', 'reply', 'owner','result',
                  'instance', 'release')
        read_only_fields = ('id', 'username', 'reply',)
        extra_kwargs = {'owner': {'write_only': True},
                        'release': {'write_only': True},
                        'instance': {'write_only': True}}




