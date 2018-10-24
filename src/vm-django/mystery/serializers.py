from rest_framework import serializers
from .models import Mystery, Instance, Release
from comments.models import Comment


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


class ReleaseSerializer(serializers.ModelSerializer):
    """
    Serializes release objects for mystery overview.

    Note:
        - Assumes that request is provided within context
    """
    commented = serializers.SerializerMethodField()

    class Meta:
        model = Release
        fields = ('number', 'commented')

    def get_commented(self, obj):
        """
        Returns true iff a user has commented on the release, otherwise returns
        false.
        """
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            instance = request.user.group.instance.all()[0].id
            comment = Comment.objects.filter(instance=instance,
                                             release=obj.number,
                                             owner=request.user.id)
            return comment.exists()
        else:
            return False


class ArtifactSerializer(serializers.ModelSerializer):
    """
    Serializes release objects for artifact view.
    """
    mystery_hash = serializers.CharField(source='mystery.hash')

    class Meta:
        model = Release
        fields = ('clue', 'hash', 'mystery_hash')


class ArtifactSerializerTA(serializers.ModelSerializer):
    """
    Serializes release objects for artifact view.
    """
    mystery_hash = serializers.CharField(source='mystery.hash')

    class Meta:
        model = Release
        fields = ('mystery', 'number', 'clue', 'hash', 'mystery_hash', 'answer')


# create a view to get answer from release
