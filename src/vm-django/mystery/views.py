from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .models import Release, Instance
from .serializers import ReleaseSerializer, ArtifactSerializer, ArtifactSerializerTA
from release import get_current_release

# Create your views here.


class ReleaseList(APIView):
    """
    Returns a list of release objects <= current release.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            current_release = get_current_release()[0]
            # checks if mystery has reached start date
            if current_release > 0:
                mystery = Instance.objects.get(group=request.user.group)\
                    .mystery
                # releases for mystery <= current_release
                releases = Release.objects.filter(mystery=mystery.id,
                                                  number__lte=current_release)
                serializer = ReleaseSerializer(releases, many=True,
                                                context={'request': request})
                # add updated response here
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Artifact(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, release):
        """
        Returns artifact information for a specific release.
        :param release: a release id, passed in the url.
        """
        try:
            current_release = get_current_release()[0]
            # checks if requested release has been reached
            if int(release) <= current_release:
                mystery = Instance.objects.get(group=request.user.group) \
                    .mystery
                release_info = Release.objects.get(mystery=mystery.id,
                                                   number=release)
                serializer = ArtifactSerializer(release_info)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # release not reached or dne
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GroupsRelaseList(APIView):
    """
    Returns a list of release objects <= current release.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, groupId):
        try:
            current_release = get_current_release()[0]
            # checks if mystery has reached start date
            if current_release > 0 and request.user.is_ta :
                mystery = Instance.objects.get(group__id=groupId).mystery
                # releases for mystery <= current_release

                releases = Release.objects.filter(mystery=mystery.id)

                serializer = ArtifactSerializerTA(releases, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
