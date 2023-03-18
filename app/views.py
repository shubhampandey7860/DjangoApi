from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def index(request):
    message = 'this is the test url '
    return Response(data = message ,status = status.HTTP_200_OK)
    

def