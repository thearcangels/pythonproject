from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Board(models.Model):
    name = model.CharField(max_length=30, unique=True)
    description = model.CharField(max_length=100)

class Topic(model.Model):
    subject = models.TextField(max_length=4000)
    topic = model.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated
