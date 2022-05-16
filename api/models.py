from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from jsonfield import JSONField

class Log(models.Model):
    """ Register model used to store all registers of service """
    
    timestamp      = models.DateTimeField(default=timezone.now, editable=False)
    data           = JSONField(default=dict)
    status_code    = models.CharField(max_length=3)
    status_message = models.CharField(max_length=150)
    user           = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.timestamp} | {self.user}: {self.status_code}"