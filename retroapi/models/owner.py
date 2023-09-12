from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField('Game', related_name='owners')
    consoles = models.ManyToManyField('Console', related_name='owners')
    controllers = models.ManyToManyField('Controller', related_name='owners')

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    