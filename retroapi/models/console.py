from django.db import models

class Console(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateField()
    description = models.TextField()
    img = models.URLField(max_length=200, null=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, related_name='condition_of_console')
