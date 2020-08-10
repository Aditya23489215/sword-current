from django.db import models

# Create your models here.

class Learning(models.Model):
    x = models.IntegerField()
    y = models.FloatField()

    def __str__(self):
        return str(self.x)
