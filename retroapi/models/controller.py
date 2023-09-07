from django.db import models

class Controller(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateField()
    description = models.TextField()
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, related_name='condition_of_controller')
