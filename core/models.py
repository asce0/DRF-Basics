from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title