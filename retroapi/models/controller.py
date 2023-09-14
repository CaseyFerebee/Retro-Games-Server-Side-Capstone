from django.db import models

class Controller(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateField()
    description = models.TextField()
    img = models.URLField(max_length=200, null=True)
