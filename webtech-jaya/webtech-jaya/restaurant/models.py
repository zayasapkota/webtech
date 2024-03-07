from django.contrib.postgres.fields import ArrayField
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=50)

    def __str__(self):
        return self.food_item
