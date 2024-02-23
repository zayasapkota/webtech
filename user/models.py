from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    ADMIN = 'admin'
    USER = 'user'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    roles = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
