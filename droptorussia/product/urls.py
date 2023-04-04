from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Page_Home.as_view(), name='home'),
    path('/<slug:url_name>', Choose_Product.as_view(), name='choose_categ'),
    path('/<slug:url_name>/<slug:filter>', Filters_Product.as_view(), name='filter_product'),
    path('/<slug:url_name>/<slug:name_categ>/<str:url_product_name>', Product_View.as_view(), name='product_view'),
    ]