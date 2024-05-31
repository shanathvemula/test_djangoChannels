from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
