from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.owner import Owner 
from ..serializers import OwnerSerializer 
# Create your views here.

# localhost :3000/owners/ get post
class OwnersView(APIView):
    """View class for owners/ for viewing all and creating """
    serializer_class = OwnerSerializer
    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response({'owners': serializer.data})
    
    def post(self, request):
        serializer = OwnerSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# local host:3000/owners/:id get delete update 
class OwnerDetailView(APIView):
    """VIEW class for owners/:pk for viewing a single owner, updating a single owner, or removing a single owner"""
    serializer_class = OwnerSerializer
    def get(self, request, pk):
        owner = get_object_or_404(Owner, pk=pk)
        serializer = OwnerSerializer(owner)
        return Response({'owner': serializer.data})

    def patch(self, request, pk):
        owner = get_object_or_404(Owner, pk=pk)
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        owner = get_object_or_404(Owner, pk=pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)