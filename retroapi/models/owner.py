from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField('Game')
    consoles = models.ManyToManyField('Console')
    controllers = models.ManyToManyField('Controller')
