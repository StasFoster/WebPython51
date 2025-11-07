from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey("MainInfo.MyUser", on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

class MyComment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("MainInfo.MyUser", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)    