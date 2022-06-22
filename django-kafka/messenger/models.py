from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey('user.User', related_name='user_message', on_delete=models.CASCADE)
    message_body = models.TextField()
    status = models.CharField(max_length=128)
