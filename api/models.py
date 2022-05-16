from django.db import models
from django.contrib.auth.models import User


class Register(models.Model):
    """ Register model used to store all registers of service """
    
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    title     = models.CharField(max_length=100)
    completed = models.BooleanField()
    
    def __str__(self):
        return f"{self.id} | {self.user}: {self.title} - {self.completed}"
