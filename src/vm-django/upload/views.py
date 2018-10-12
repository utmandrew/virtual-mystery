from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser

class upload(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def post(self, request, filename):
        try:
            print(filename)
            print(request.data['file'])
            #note the actull file writer need to fixed and need to create directories for each user etc
            #handle_uploaded_file(request.data['file'])
            return Response(status=status.HTTP_201_CREATED)
        except AttributeError:
            # catches if an attribute does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            # catches if an object (instance) does not exist
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return  Response(status=status.HTTP_400_BAD_REQUEST)

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
