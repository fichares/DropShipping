from django.db import models
from transliterate import get_available_language_codes, translit


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class My_product(models.Model):
    categ = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url_name = models.URLField(default='')
    release_date = models.DateField()
    price = models.IntegerField()
    description = models.TextField()
    gender = models.TextField(default='men')
    articules = models.IntegerField(unique=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.url_name = translit(self.name, language_code='ru', reversed=True).replace(' ', '_')
        super(My_product, self).save()
