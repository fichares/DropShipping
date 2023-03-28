from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Page_Home.as_view(), name='home'),
    path('/<slug:url_name>', Choose_Product.as_view(), name='choose_categ'),
    ]