from rest_framework import serializers

from .models.dog import Dog
from .models.owner import Owner

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Dog

class OwnerReadSerializer(serializers.ModelSerializer):
    dog = serializers.StringRelatedField()
    class Meta: 
        fields = '__all__'
        model = Dog

class OwnerSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Owner