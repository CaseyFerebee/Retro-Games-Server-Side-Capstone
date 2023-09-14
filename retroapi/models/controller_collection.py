from django.db import models

class ControllerCollection(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='created_controller')
    controller = models.ForeignKey('Controller', on_delete=models.CASCADE, related_name='controller_collection')
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, related_name='controller_condition')