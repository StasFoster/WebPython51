from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Thread(models.Model):
    title = models.CharField()
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("MainInfo.MyUser", on_delete=models.CASCADE)

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("MainInfo.MyUser", on_delete=models.CASCADE)
