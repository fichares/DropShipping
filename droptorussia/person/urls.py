from django.urls import path, re_path
from .views import *

urlpatterns = [
#     path('person=/<slug:name>', Personal_Account.as_view(), name='personal_account'),
     path('login', LoginUser.as_view(), name='login'),
     path('registration', RegisterUser.as_view(), name='register'),
     path('', Home_Auntificate_User.as_view(), name='home_user'),
     path('personal_account', Personal_Account.as_view(), name='personal_account'),
     path('liked', Liked.as_view(), name='liked'),
     path('choose_product', Choose_Product.as_view(), name='choose_product'),
    ]