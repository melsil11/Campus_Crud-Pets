from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.appointment import Appointment
from ..serializers import AppointmentSerializer, AppointmentReadSerializer


class AppointmentsView(APIView):
    """View class for Appointments/ for viewing all and creating"""
    serializer_class = AppointmentSerializer
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentReadSerializer(appointments, many=True)
        return Response({'appointments': serializer.data})

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:8000/library/Appointments/:id get delete update
class AppointmentDetailView(APIView):
    """View class for Appointments/:pk for viewing a single Appointment, updating a single Appointment, or removing a single Appointment"""
    serializer_class = AppointmentSerializer
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        serializer = AppointmentReadSerializer(appointment)
        return Response({'appointment': serializer.data})

    def patch(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)