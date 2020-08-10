from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    profile_pic=models.ImageField(default='default.jpg',upload_to='profile_img')

    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height>300 and img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
