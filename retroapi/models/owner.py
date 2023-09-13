from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField('Game', through='GameCollection')
    controllers = models.ManyToManyField('Controller', through='ControllerCollection')
    consoles = models.ManyToManyField('Console', through='ConsoleCollection')


    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    