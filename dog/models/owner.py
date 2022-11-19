from django.db import models
from .dog import Dog

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE,
        related_name='dogs'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.dog}"