from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50, null=True)
    phone=models.CharField(max_length=50, null=True)
    organization=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    profilePicture=models.ImageField(default="img_avatar1.png", null=True, blank=True)
    user=models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


