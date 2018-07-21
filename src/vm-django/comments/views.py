from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .serializers import CommentCreateSerializer, ReplyCreateSerializer, \
    CommentViewSerializer
from .models import Comment
from mystery.models import Instance


# Create your views here.

class CommentList(APIView):
    """
    Returns a list of comment objects.

    Notes:
        - Add support for release (clue)
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Returns a list of comment form the users instance.
        """
        try:
            instance = request.user.profile.group.instance.all()[0].id
            comments = Comment.objects.filter(instance=instance)
        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentViewSerializer(comments, many=True)
        return Response(serializer.data)


    # def post(self, request):
    #     """
    #     Returns a list of comments based on the release/clue number sent.
    #
    #     Notes:
    #          - check if the release/clue has been released
    #
    #     """
    #     pass


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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

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
