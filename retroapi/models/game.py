from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    releaseDate = models.DateField()
    publisher = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    modes = models.CharField(max_length=255)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, related_name='condition_of_game')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='genre_of_game')
