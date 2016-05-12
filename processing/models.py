from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Message(models.Model):
    message=models.CharField(max_length=100, unique=False)
    date=models.DateField(default=datetime.now, blank=False)

    def __unicode__(self):
        return self.message