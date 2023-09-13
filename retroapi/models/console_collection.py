from django.db import models

class ConsoleCollection(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='created_console')
    console = models.ForeignKey('Console', on_delete=models.CASCADE)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE)