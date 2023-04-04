from django.urls import path, re_path
from .views import *

urlpatterns = [
#     path('person=/<slug:name>', Personal_Account.as_view(), name='personal_account'),
     path('login', LoginUser.as_view(), name='login'),
     path('logout', logout_user, name='logout'),
     path('registration', RegisterUser.as_view(), name='register'),
     path('', Home_Auntificate_User.as_view(), name='home_user'),
     path('personal_account/<slug:username>', Personal_Account.as_view(), name='personal_account'),
     path('liked', Liked.as_view(), name='liked'),
     path('choose_product', In_the_basket.as_view(), name='choose_product'),
     path('add_liked_product/<slug:product_id>', Add_Liked_Product.as_view(), name='add_liked'),
     path('add_liked_product/<slug:filter>', Filters_Product_Liked_Product.as_view(), name='filters_add_liked'),
    ]