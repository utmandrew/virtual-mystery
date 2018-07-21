from django.core.exceptions import ObjectDoesNotExist
from .serializers import CommentCreateSerializer, ReplyCreateSerializer
from .models import Comment
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from mystery.models import Instance


# Create your views here.


class CommentCreate(APIView):
    """
    Creates a new comment.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Creates a comment through info submitted in a post request.

        Note:
            - Add support for release (clue)
            - Add required error checks

        """

        try:
            data = request.data
            data['owner'] = request.user.pk
            data['instance'] = Instance.objects.filter(
                group=request.user.profile.group.id)[0].id
            serializer = CommentCreateSerializer(data=data)
        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            # creates comment
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ReplyCreate(APIView):
    """
    Creates a new reply.
    """

    def post(self, request):
        """
        Creates a reply to a comment through info submitted in a post request.
        """

        try:
            data = request.data
            # current user instance
            instance = Instance.objects.filter(
                group=request.user.profile.group.id)[0].id

            # checks if reply owner and reply parent are in the same instance
            if (Comment.objects.filter(owner=data['parent'],
                                       instance=instance)):
                data['owner'] = request.user.pk
                serializer = ReplyCreateSerializer(data=data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            # creates comment
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
