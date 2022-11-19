from .serializers import CatSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cat 
# Create your views here.

# localhost :3000/cats/ get post
class CatsView(APIView):
    """View class for cats/ for viewing all and creating """
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response({'cats': serializer.data})
    
    def post(self, request):
        serializer = CatSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# local host:3000/cats/:id get delete update 
class CatDetailView(APIView):
    """VIEW class for cats/:pk for viewing a single cat, updating a single cat, or removing a single cat"""
    def get(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        serializer = CatSerializer(cat)
        return Response({'cat': serializer.data})

    def patch(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   