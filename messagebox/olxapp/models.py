from django.db import models
from django.db.models import CASCADE
from django.utils import timezone


class Conversation(models.Model):
    external_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField()


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=CASCADE)
    external_id = models.IntegerField(unique=True)
    message = models.TextField()
    created_at = models.DateTimeField()


class Answer(models.Model):
    title = models.CharField(max_length=100)
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
