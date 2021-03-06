import logging

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password, \
    get_password_validators
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from mystery.models import Instance
from release import get_current_release

activityLogger = logging.getLogger('activity')
debugLogger = logging.getLogger('debug')


# Create your views here.


class Login(ObtainAuthToken):
    """
    Custom User Login.
    Returns user token and other required information, otherwise returns
    http_400_bad_request.
    """

    def post(self, request, *args, **kwargs):
        username = ''
        try:
            # checks if user credentials are correct
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # successfully authenticated
                token, created = Token.objects.get_or_create(user=user)

                # get current release info
                release_info = get_current_release()

                # log successful login
                activityLogger.info(f'Login: User "{username}" logged in.')

                return Response({
                    'token': token.key,
                    'release': release_info[0],
                    'mark': release_info[1],
                    'mystery_end': release_info[2],
                    'is_ta': user.is_ta
                }, status=status.HTTP_200_OK)

            else:
                # authentication failed
                activityLogger.error(f'Failed login: User "{username}" failed authentication.')
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            debugLogger.exception(f'User "{username}" login failed.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            debugLogger.exception(f'User "{username}" login failed.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            debugLogger.exception(f'User "{username}" login failed.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    """
    User Logout.
    Deletes the user token (server side) to force a login.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        username = ''
        try:
            username = request.user.get_username()
            request.user.auth_token.delete()
            activityLogger.info(f'Logout: User "{username}" logged out.')
        except AttributeError:
            debugLogger.exception(f'User "{username}" failed to log out.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class ChangePassword(APIView):
    """
    User Password Change.
    Changes authenticated user password, deleting the user token (server side)
    if successful, forcing a logout.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        username = ''
        try:
            user = request.user
            username = request.user.get_username()
            new_password = request.data['new_password']
            confirm_password = request.data['confirm_password']
            # required password validator configuration
            validator_config = [
                {
                    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                    'OPTIONS': {'min_length': 8}
                }
            ]

            # check to see if password confirmation matches with new password
            if new_password == confirm_password:
                # gets password validators
                validators = get_password_validators(validator_config)
                # validates password (raises ValidationError if invalid)
                validate_password(new_password,
                                  user=user,
                                  password_validators=validators)
                # sets and saves new password for user
                user.set_password(new_password)
                user.save()

                # log password change
                activityLogger.info(f'Password change: User "{username}" changed password.')
                return Response(status=status.HTTP_200_OK)
            else:
                # log unsuccessful password change
                activityLogger.info(f'Failed password change: User "{username}" attempted to '
                                    f'change their password but did not enter matching passwords.')
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except AttributeError:
            debugLogger.exception(f'User "{username}" password change failed.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            debugLogger.exception(f'User "{username}" password change failed.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            debugLogger.exception(f'User "{username}" password change failed.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            debugLogger.exception(f'User "{username}" password change failed.', exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
