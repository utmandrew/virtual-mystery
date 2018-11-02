from math import floor
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from mystery.models import Instance
from release import get_current_release

# Create your views here.


class Login(ObtainAuthToken):
    """
    Custom User Login.
    Returns user token and other required information, otherwise returns
    http_400_bad_request.

    Notes: add support for ta/admin accounts

    """

    def post(self, request, *args, **kwargs):
        try:
            # checks if user credentials are correct
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # successfully authenticated
                token, created = Token.objects.get_or_create(user=user)
                release = floor(get_current_release())
                # mystery = Instance.objects.get(group=user.group).mystery.hash
                return Response({
                    'token': token.key,
                    'release': release,
                    'is_ta': user.is_ta
                    # 'mystery': mystery
                }, status=status.HTTP_200_OK)

            else:
                # authentication failed
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    """
    User Logout.
    Deletes the user token (server side) to force a login.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
