from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.dog import Dog 
from ..serializers import DogSerializer
# Create your views here.

# localhost :3000/dogs/ get post
class DogsView(APIView):
    """View class for dogs/ for viewing all and creating """
    serializer_class = DogSerializer
    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response({'dogs': serializer.data})
    
    def post(self, request):
        serializer = DogSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# local host:3000/dogs/:id get delete update 
class DogDetailView(APIView):
    """VIEW class for dogs/:pk for viewing a single dog, updating a single dog, or removing a single dog"""
    serializer_class = DogSerializer
    def get(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        return Response({'dog': serializer.data})

    def patch(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   