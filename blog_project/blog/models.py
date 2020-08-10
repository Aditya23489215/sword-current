from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    # if we want to update the date then we can use auto_now=True and if we want to fix the date then we can use default=timezone.now
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.id})

class Reply(models.Model):
    to_reply = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=400)
    left_margin = models.IntegerField(default=0)
    color_style = models.CharField(max_length=300, default="w3-flat-nephritis")
    postId = models.IntegerField(blank=True, null=True)
