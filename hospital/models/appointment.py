from  django.db import models
from .doctor import Doctor
from .patient import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor, 
        on_delete=models.CASCADE)

    scheduled_appointment = models.DateField()
    
    def __str__(self):
        return self.scheduled_appointment