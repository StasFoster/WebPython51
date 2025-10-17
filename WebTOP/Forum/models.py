from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey("MainInfo.MyUser", on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title