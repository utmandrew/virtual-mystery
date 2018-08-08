from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .models import Release, Instance
from .serializers import ReleaseSerializer
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
            current_release = get_current_release()
            # checks if mystery has reached start date
            if current_release > 0:
                mystery = Instance.objects.get(group=request.user.group)\
                    .mystery
                # releases for mystery <= current_release
                releases = Release.objects.filter(mystery=mystery.id,
                                                  number__lte=current_release)
                serializer = ReleaseSerializer(releases, many=True,
                                                context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
