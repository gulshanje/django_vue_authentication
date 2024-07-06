from django.db import models

# Create your models here.
class Vehicle(models.Model):
    model_year = models.CharField(max_length=6)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    rejection_percentage = models.CharField(max_length=5)
    reason_1 = models.CharField(max_length=250)
    reason_2 = models.CharField(max_length=250)
    reason_3 = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.make)
