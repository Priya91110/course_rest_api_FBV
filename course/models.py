from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField()
    authername = models.CharField(max_length=100)
        