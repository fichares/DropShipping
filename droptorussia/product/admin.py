from django.contrib import admin

from .models import Category, My_product

admin.site.register(Category)

@admin.register(My_product)
class My_Product_Admin(admin.ModelAdmin):
    fields = ['categ', 'name', 'release_date',
              'price', 'description', 'gender', 'articules',
              'photo']