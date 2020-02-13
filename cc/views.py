# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Excursion
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExcursionSerializer
from rest_framework.views import APIView
from rest_framework import status


# def hello(request):
#     return HttpResponse('Hello')

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello'}
        return Response(content)


class ExcursionList(APIView):
    #protecting views from users without access token
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        # excursions=Excursion.objects.()
        
        # using raw sql query commands
        excursions=Excursion.objects.raw('SELECT * FROM cc_excursion WHERE 1')

        data=ExcursionSerializer(excursions,many=True).data
        return Response(data, status=status.HTTP_200_OK)

class SingleExcursion(APIView):
    #protecting views from users without access token
    # permission_classes = (IsAuthenticated,)
    
    def get(self,request,id):
        excursion=Excursion.objects.get(id=id)
        
        # using raw sql query commands
        # excursion=Excursion.objects.raw(f"SELECT * FROM cc_excursion WHERE id={id}")

        data=ExcursionSerializer(excursion).data
        return Response(data, status=status.HTTP_200_OK)

class CreateExcursion(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ExcursionSerializer

    def post(self, request):
        data = {
        }
        serializer = ExcursionSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)