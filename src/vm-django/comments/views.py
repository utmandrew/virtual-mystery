from django.core.exceptions import ObjectDoesNotExist
from .serializers import CommentCreateSerializer
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





