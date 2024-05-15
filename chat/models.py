from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=1000)  # Changed to TextField
    date = models.DateTimeField(default=datetime.now, blank=True)  # Removed () after datetime.now
    user = models.CharField(max_length=255)  # Reduced max_length
    room = models.CharField(max_length=255)  # Reduced max_length
