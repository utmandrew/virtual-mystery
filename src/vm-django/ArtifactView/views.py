from django.shortcuts import render

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

from release import get_current_release

from . import serializers
from .serializers import HelloSerializer

from . import models


class ArtifactViewData(APIView):
    """
    Return all the data related to the artifact viewing for a single person

    """

    serializer_class = serializers.HelloSerializer
    permission_classes = (permissions.IsAuthenticated,)

    image="image1.jpg"
    clue = "clue.txt"
    answer = "ans.txt"
    
    def get(self, request, format=None):
        
        print("checkpoint 1")

        current_week = get_current_release()
        path_image = "assets/anthro-virtual-mysteries/Archaeology-demo/"
        path_clue = "assets/anthro-virtual-mysteries/Archaeology-demo/"
        path_answer = "assets/anthro-virtual-mysteries/Archaeology-demo/"

        path_image += str(request.user.group.mystery1) + "/Release" +str(current_week) +"/image1.jpg"
        path_clue += str(request.user.group.mystery1) + "/Release" +str(current_week)+"/clue.txt"
        path_answer += str(request.user.group.mystery1) + "/Release" +str(current_week)+ "/ans.txt"

        return Response({
                    'user': str(request.user),
                    'group': str(request.user.group.mystery1),
                    'image': path_image,
                    'clue': path_clue,
                    'answer': path_answer, 
                    }, 
                    status=status.HTTP_200_OK)
