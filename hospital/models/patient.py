from django.db import models
from .doctor import Doctor

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    diagnoses = models.CharField(max_length=100)
    born_on = models.CharField(max_length=100)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='doctor'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.born_on} {self.diagnoses} {self.doctor}"