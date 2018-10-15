from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .serializers import ReplySerializer, CommentSerializer, ResultSerializer
from .models import Comment
from mystery.models import Instance
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
            instance = request.user.group.instance.all()[0].id
            commented = Comment.objects.filter(instance=instance,
                                        release=release, owner=request.user.id)
            current_release = get_current_release()

            # checks if user has commented on the current release
            if request.user.is_ta or commented or int(release) < current_release:
                comments = Comment.objects.filter(instance=instance,
                                                  release=release)
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # if requested release has not yet been reached
                # if int(release) > current_release:
                #     return Response(status=status.HTTP_400_BAD_REQUEST)
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
            instance = request.user.group.instance.all()[0].id
            release = get_current_release()
            commented = Comment.objects.filter(instance=instance,
                                          release=release,
                                          owner=request.user.id).exists()

            # checks if mystery start date has been reached
            if release > 0:
                # checks if user has already commented
                if not commented:
                    # (.copy returns a mutable QueryDict object)
                    data = request.data.copy()
                    data['owner'] = request.user.id
                    data['instance'] = instance
                    data['release'] = release


                    serializer = CommentSerializer(data=data)
                    print(serializer)
                    if serializer.is_valid():
                        # creates comment
                        serializer.save()
                        return Response(status=status.HTTP_201_CREATED)
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
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
            # (.copy returns a mutable QueryDict object)
            data = request.data.copy()
            # current user instance
            instance = request.user.group.instance.all()[0].id
            print(data)
            # checks if reply owner and parent comment are in the same instance
            if Comment.objects.filter(instance=instance, id=data.get('parent',
                                                                     None)):
                data['owner'] = request.user.id
                print(data)
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


class TaCommentList(APIView):
    """
    Returns a list of comment objects.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, release, groupName):
        """
        Returns a list of comments from the users instance and specified
        release.
        :param release: a release id, passed in the url.
        """

        try:
            instance = Instance.objects.filter(group__name=groupName).first()
            commented = Comment.objects.filter(instance=instance.id,
                                        release=release, owner=request.user.id)
            current_release = get_current_release()

            # checks if user has commented on the current release
            if request.user.is_ta or commented or int(release) < current_release:
                comments = Comment.objects.filter(instance=instance,
                                                  release=release)
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # if requested release has not yet been reached
                # if int(release) > current_release:
                #     return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_403_FORBIDDEN)

        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ResultCreate(APIView):
    """
    All the Result Objects the t.a has made
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request):
        """
        Creates a Result for a certain comment
        """
        try:
            # check if user is ta
            data = request.data.copy()

            if request.user.is_ta:
                data['owner'] = request.user.username
                print(data)
                serializer = ResultSerializer(data=data)

        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        


        



    
