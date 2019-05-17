from django.db import models

# Create your models here.

class CarSet(models.Model):
    car_name = models.CharField(max_length=255)
    mpg = models.DecimalField(max_digits=6, decimal_places=2)
    cylinders = models.IntegerField()
    displacement = models.DecimalField(max_digits=6, decimal_places=2)
    horsepower = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    acceleration = models.DecimalField(max_digits=6, decimal_places=2)
    model = models.IntegerField()
    origin = models.CharField(max_length=10)

    def __str__(self):
        return self.car_name
