from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class My_product(models.Model):
    categ = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    price = models.IntegerField()
    description = models.TextField()
    articules = models.IntegerField()
    photo = models.ImageField()

    def __str__(self):
        return self.name