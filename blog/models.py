from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    text = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
