from django.db import models

class GameCollection(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='created_game')
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE)