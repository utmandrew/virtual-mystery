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

from release import get_current_release




from . import models
from mystery.models import Mystery,Release



class ArtifactViewData(APIView):
    """
    Return all the data related to the artifact viewing for a single person

    """


    permission_classes = (permissions.IsAuthenticated,)


    def get(self, request, format=None):
        


        current_week = get_current_release()

        # now releases are contricted in 1-3
        
        if (current_week % 3) == 0:
            current_week = 3
        elif current_week % 3 == 1:
            current_week = 1
        elif current_week % 3 == 2:
            current_week = 2

        # we need to work on implenting which order of mysteries to release in which order
        # for time being it is this particular mystery object 
        mystery_name = Mystery.objects.get(pk=1)

        mystery_ob = Release.objects.get(pk=current_week)
        #print( Release.objects.get(pk=1))


        # Need to implement a method to assign mysteries to groups in a list format
        # so we can figure which mysteries to release in which order
        # later implement a method to organize all 1-9 releases for a student so we can 
        # easily navigate between next, previous releases/weeks

        # also need to create a python file which well read all text files and create
        # release objects extracting the clue/answer text and putting it in the db

        # not currently storing images in db so we must use a path in front end

        path_image = "assets/anthro-virtual-mysteries/Archaeology-demo/"
        #path_clue = "assets/anthro-virtual-mysteries/Archaeology-demo/"
        path_clue = mystery_ob.clue
        #path_answer = "assets/anthro-virtual-mysteries/Archaeology-demo/"
        path_answer = mystery_ob.answer


        path_image += str(mystery_name.name) + "/Release" +str(current_week) +"/image1.jpg"
        #path_clue += str(request.user.group.mystery1) + "/Release" +str(current_week)+"/clue.txt"
        #path_answer += str(request.user.group.mystery1) + "/Release" +str(current_week)+ "/ans.txt"


        #Release.objects.filter(mystery=users_mystery, release=required_release)
        return Response({
                    'user': str(request.user),
                    'mystery': str(mystery_name.name),
                    'image': path_image,
                    'clue': path_clue,
                    'answer': path_answer, 
                    }, 
                    status=status.HTTP_200_OK)
