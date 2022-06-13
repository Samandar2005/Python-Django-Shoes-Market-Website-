from rest_framework import serializers
from home.models import Shoes


class ShoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoes
        fields = '__all__'
