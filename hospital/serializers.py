from rest_framework import serializers

from .models.doctor import Doctor
from .models.patient import Patient
from .models.appointment import Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Doctor

class PatientReadSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Doctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Patient

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentReadSerializer(AppointmentSerializer):
    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField() 
    class Meta:
        fields = '__all__'
        model = Appointment