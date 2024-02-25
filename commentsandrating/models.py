from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class CommentNRating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5)
    ])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
