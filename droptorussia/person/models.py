from django.db import models
from django.contrib.auth.models import AbstractUser

from product.models import My_product


class User(AbstractUser):
    photo = models.ImageField(default='photo_default_user.png')
    adress = models.TextField(max_length=80, default='')


class Liked_Product(models.Model):
    wh_user = models.ForeignKey(User, on_delete=models.CASCADE)
    wh_product = models.ForeignKey(My_product, on_delete=models.CASCADE, unique=True)
    data_add = models.TimeField(auto_now=True)

