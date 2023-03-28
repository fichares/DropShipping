from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView
from .forms import *
from .models import User
from product.views import Page_Home




class Personal_Account(TemplateView):

    template_name = 'person/personal_account.html'


class Liked(TemplateView):

    template_name = 'person/personal_account.html'

class Choose_Product(TemplateView):

    template_name = 'person/personal_account.html'






class LoginUser(LoginView, Page_Home):
    form_class = LoginUserForm
    template_name = 'person/login_user.html'

    def get_success_url(self):
        return reverse_lazy("home_user")


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'person/register_user.html'


    def form_valid(self, form):
        get_user_model().user = form.save()
        login(self.request, get_user_model().user)
        slug = form.username
        return redirect('home_user')


class Home_Auntificate_User(Page_Home):
    template_name = 'person/home_auntificate_user.html'




def logout_user(request):
    logout(request)
    return redirect('home')