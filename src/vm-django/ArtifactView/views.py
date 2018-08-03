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
        
        return Response({
                    'images': image,
                    'clue': mystery,
                    'answer': answer}, 
                    status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})
    



    


