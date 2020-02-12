from rest_framework import serializers
from .models import Excursion

class ExcursionSerializer(serializers.ModelSerializer):
    # user=UserSerializer(many=True,required=False)
    class Meta:
        model= Excursion
        fields="__all__"
