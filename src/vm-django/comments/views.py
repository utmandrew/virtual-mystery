from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .serializers import ReplySerializer, CommentSerializer
from .models import Comment
# from mystery.models import Instance
from release import get_current_release


# Create your views here.

class CommentList(APIView):
    """
    Returns a list of comment objects.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, release):
        """
        Returns a list of comments from the users instance and specified
        release.
        :param release: a release id, passed in the url.
        """

        try:
            instance = request.user.profile.group.instance.all()[0].id

            # checks if user has commented on the current release
            if Comment.objects.filter(instance=instance, release=release,
                                      owner=request.user.id):
                comments = Comment.objects.filter(instance=instance,
                                                  release=release)
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentCreate(APIView):
    """
    Creates a new comment.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Creates a comment through info submitted in a post request.
        """
        try:
            instance = request.user.profile.group.instance.all()[0].id
            release = get_current_release()
            commented = Comment.objects.filter(instance=instance,
                                          release=release,
                                          owner=request.user.pk).exists()
            # checks if user has already commented
            if not commented and release > 0:
                data = request.data
                data['owner'] = request.user.id
                data['instance'] = instance
                data['release'] = release
                serializer = CommentSerializer(data=data)
                if serializer.is_valid():
                    # creates comment
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ReplyCreate(APIView):
    """
    Creates a new reply.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Creates a reply to a comment through info submitted in a post request
        and returns the newly created reply.
        """

        try:
            # data sent in post request
            data = request.data

            # current user instance
            instance = request.user.profile.group.instance.all()[0].id

            # checks if reply owner and parent comment are in the same instance
            if Comment.objects.filter(instance=instance, id=data['parent']):
                data['owner'] = request.user.id
                serializer = ReplySerializer(data=data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            # creates reply
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
