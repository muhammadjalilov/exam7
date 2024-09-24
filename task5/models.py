from django.db import models

from task1.models import User


class Post(models.Model):
    title = models.CharField(max_length=128, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
