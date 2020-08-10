from django.db import models
from django.urls import reverse
from PIL import Image

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    image = models.ImageField(default='Anime_12.jpg',upload_to='products')
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store_item', kwargs={'pk':self.id})

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_query_name='orders')
    quantity = models.IntegerField(default=1)

    @property
    def total(self):
        total = 0
        for order in User.objects.all().filter(id=self.customer.id).first().order_set.all():
            total += order.product.price * order.quantity
        return total

    
