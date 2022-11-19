from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.doctor import Doctor 
from ..serializers import DoctorSerializer
# Create your views here.

# localhost :3000/doctors/ get post
class DoctorsView(APIView):
    """View class for doctors/ for viewing all and creating """
    serializer_class = DoctorSerializer
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response({'doctors': serializer.data})
    
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# local host:3000/books/:id get delete update 
class DoctorDetailView(APIView):
    """VIEW class for doctors/:pk for viewing a single doctor, updating a single doctor, or removing a single doctor"""
    serializer = DoctorSerializer
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response({'doctor': serializer.data})

    def patch(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CON)