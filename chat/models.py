from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_msg')
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.author, self.date)


