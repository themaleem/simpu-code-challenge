# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Excursion
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExcursionSerializer
from rest_framework.views import APIView
from rest_framework import status,generics

class ExcursionList(generics.ListCreateAPIView):
    #protecting views from users without access token
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        # using raw sql query commands
        excursions=Excursion.objects.raw('SELECT * FROM cc_excursion WHERE 1')
        return excursions
        
    serializer_class=ExcursionSerializer

class SingleExcursion(generics.RetrieveDestroyAPIView):
    #protecting views from users without access token
    # permission_classes = (IsAuthenticated,)
    
    queryset=Excursion.objects.all()
    serializer_class=ExcursionSerializer
    
    # def get_queryset(self):
    #     excursions=Excursion.objects.all()

    #     # using raw sql query commands
        # excursions=Excursion.objects.raw('SELECT * FROM cc_excursion WHERE 1')
        # return excursions
