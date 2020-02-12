# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Excursion
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExcursionSerializer
from rest_framework.views import APIView


# def hello(request):
#     return HttpResponse('Hello')

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello'}
        return Response(content)


class ExcursionList(APIView):
    def get(self,request):
        excursions=Excursion.objects.all()
        data=ExcursionSerializer(excursions,many=True).data
        return Response(data)