from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class Event(models.Model):
    data = models.TextField()
    description = models.TextField()

class MyUser(AbstractUser):
    pass