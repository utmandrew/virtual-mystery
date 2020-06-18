import logging

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .serializers import ReplySerializer, CommentSerializer, ResultSerializer, TACommentSerializer
from .models import Comment, Result
from mystery.models import Instance
# from mystery.models import Instance
from release import get_current_release

activityLogger = logging.getLogger('activity')
debugLogger = logging.getLogger('debug')


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
                                               release=release,
                                               owner=request.user.id).exists()
            release_info = get_current_release()

            # checks if user has commented on the current release
            if commented or int(release) < release_info[0] or release_info[1] \
                    or release_info[2]:
                comments = Comment.objects.filter(instance=instance,
                                                  release=release)
                serializer = CommentSerializer(comments, many=True)
                # add updated response here
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # add updated response here
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
            release_info = get_current_release()
            commented = Comment.objects.filter(instance=instance,
                                               release=release_info[0],
                                               owner=request.user.id).exists()

            # checks if mystery start date has been reached
            if release_info[0] > 0:
                # checks if user has already commented
                if not commented and \
                        (not release_info[1] or not release_info[2]):
                    # (.copy returns a mutable QueryDict object)
                    data = request.data.copy()
                    data['owner'] = request.user.id
                    data['instance'] = instance
                    data['release'] = release_info[0]

                    serializer = CommentSerializer(data=data)

                    if serializer.is_valid():
                        # creates comment
                        serializer.save()
                        return Response(status=status.HTTP_201_CREATED)
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    # add updated response here
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

            # checks if reply owner and parent comment are in the same instance
            if Comment.objects.filter(instance=instance, id=data.get('parent',
                                                                     None)):
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


class TaCommentList(APIView):
    """
    Returns a list of comment objects.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, release, groupId):
        """
        Returns a list of comments from the users instance and specified
        release.
        :param release: a release id, passed in the url.
        """

        try:
            instance = Instance.objects.filter(group__id=groupId).first()
            current_release = get_current_release()[0]

            # check if user is a ta to get the release
            if request.user.is_ta or int(release) < current_release:
                comments = Comment.objects.filter(instance=instance,
                                                  release=release)
                serializer = TACommentSerializer(comments, many=True)
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

    def post(self, request):
        """
        Creates a Result for a certain comment
        """
        username = ''
        data = {}
        try:

            # check if user is ta
            data = request.data.copy()
            comment = Comment.objects.get(id=request.data.get('id'))
            username = request.user.get_username()

            # #Update the result
            if comment.marked:
                Result.objects.filter(comment=comment).update(mark=data['mark'], feedback=data['feedback'])

                # log the result update
                activityLogger.info(f'Result updated ({username}): {data}')
                return Response(status=status.HTTP_201_CREATED)

            # Create a result
            if request.user.is_ta and not comment.marked:
                data['owner'] = username
                data['comment'] = comment.id

                serializer = ResultSerializer(data=data)
                if serializer.is_valid():
                    Comment.objects.filter(id=comment.id).update(marked=True)
                    serializer.save()

                    # log the result creation
                    activityLogger.info(f'Result created ({username}): {data}')
                    return Response(status=status.HTTP_201_CREATED)
                # otherwise, log unsuccessful result creation
                debugLogger.debug(f'Unsuccessful result create ({username}): {data}')
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except AttributeError:
            debugLogger.exception(f'User "{username}" result create failed: {data}', exc_info=True)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            debugLogger.exception(f'User "{username}" result create failed: {data}', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            debugLogger.exception(f'User "{username}" result create failed: {data}', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # should never reach here
        debugLogger.debug(f'Student "{username}" tried to assign a mark.')
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserResult(APIView):
    """
    Sends the User's Result for the indicated week
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        try:

            results = Result.objects.get(comment__owner=request.user,
                                         comment__release=get_current_release()[0])
            serializer = ResultSerializer(results)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserGradesList(APIView):
    """
    Sends the User's Result for the indicated week
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        try:

            # results = Result.objects.get(comment__owner=request.user, comment__release = get_current_release())
            comments = Comment.objects.filter(owner=request.user)

            serializer = TACommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TaCommentCreate(APIView):
    """
    Creates a new comment.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Creates a comment through info submitted in a post request.
        """

        instance = Instance.objects.filter(group=request.data['group'], mystery=request.data['mystery']).first()
        release = request.data['release']
        # checks if mystery start date has been reached
        if release > 0:
            # (.copy returns a mutable QueryDict object)
            data = request.data.copy()
            data['owner'] = request.user.id
            data['instance'] = instance.id
            data['release'] = release

            username = request.user.get_username()

            serializer = CommentSerializer(data=data)

            if serializer.is_valid():
                # creates comment
                serializer.save()

                # log successful TA comment
                activityLogger.info(f'TA comment ({username}): {data}')
                return Response(status=status.HTTP_201_CREATED)
            # otherwise, log unsuccessful comment data
            debugLogger.debug(f'Unsuccessful TA comment ({username}): {data}')
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            debugLogger.debug('Attempted to create TA comment before mystery start date.')
            return Response(status=status.HTTP_400_BAD_REQUEST)
