from django.contrib.postgres.fields import ArrayField
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length = 15)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    Delivery = models.BooleanField(default = True)
    location = models.URLField(default = "")
    cover = models.ImageField(name="cover")
    menu = models.ImageField(name = "menu")

    def __str__(self):
        return self.name



