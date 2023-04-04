from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Liked_Product

admin.site.register(User)
admin.site.register(Liked_Product)
