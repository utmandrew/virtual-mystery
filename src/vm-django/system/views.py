from django.shortcuts import render
from django.db import models

from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import models
from system.models import Practical, Group, User
from comments.models import Comment
from .serializers import PracticalSerializer, GroupSerializer, ProfileSerializer
from comments.serializers import CommentSerializer

from release import get_current_release

class ListPracticals(APIView):
    """
    Return list of all practical objects
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        # TO DO: need to send all names for all practicals
        try:
            if request.user.is_ta:
                practical_list = Practical.objects.all()
                #
                serializer = PracticalSerializer(practical_list, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListGroups(APIView):
    """
    Take a Practical name as input and return all groups
    that are in that practical
    """
    def get(self,request,praName):
        # TO DO: need to send all names for all groups

        practical = Practical.objects.filter(name= praName).first()

        group = Group.objects.filter(practical = practical)


        serializer = GroupSerializer(group,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ListUsers(APIView):
    """
    Take a Practical name as input and return all groups
    that are in that practical
    """
    def get(self,request, groupName):
        # TO DO: need to send all names for all groups

        group = Group.objects.filter(name = groupName).first()

        users = User.objects.filter(group=group)

        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserCheck(APIView):
    """
    Checks if the user is a TA or not
    """
    def get(self,request ,Formant=None):
        user = request.user.is_ta
        return Response ({'is_ta':user}, status=status.HTTP_200_OK)

class UserComment(APIView):
    """
    Take a Practical name as input and return all groups
    that are in that practical
    """
    def get(self,request, userName):
        #Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
        selectedUser = User.objects.get(username=userName)
        selectedComment = Comment.objects.filter(owner= selectedUser)

        serializer = CommentSerializer(selectedComment,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)