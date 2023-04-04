from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, FormView, UpdateView
from .forms import *
from .models import User, Liked_Product
from product.views import Page_Home, DataMixin, Filters_Product

from product.models import My_product, Category


class Personal_Account(UpdateView):
    template_name = 'person/personal_account.html'
    form_class = UserProfile
    model = User
    pk_url_kwarg = 'username'

  #  def get_success_url(self):
   #     return redirect("home_user")

 #   def form_invalid(self, form):
 #       print('Error')
#        return redirect('home_user')

    def form_valid(self, form):
        portfolio = form.save(commit=False)
        portfolio.save()
        return redirect("home_user")

class Add_Liked_Product(Page_Home):

    def get_context_data(self, *args, **kwargs):
        context = super(Add_Liked_Product, self).get_context_data(*args, **kwargs)
        artic_product = self.kwargs['product_id']
        user_id = self.request.user
   #     print(artic_product, self.request.user.pk)
        Liked_Product.objects.create(wh_user=user_id, wh_product=My_product.objects.filter(id=artic_product).first())

    def get_success_url(self):
        return reverse_lazy("home_user")



class Liked(Page_Home):

    template_name = 'person/liked.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Liked, self).get_context_data(*args, **kwargs)
        pr_e = Liked_Product.objects.filter(wh_user=self.request.user)
        mas = []
        for e in pr_e:
            mas.append(e.wh_product)

        print(mas)
        context['product'] = mas #    Liked_Product.objects.filter(wh_user=self.request.user)
        context['categ_product'] = Category.objects.all()
        context['menu'] = self.menu
      #  context['now_categ'] = self.kwargs['url_name']
        return context


class Filters_Product_Liked_Product(Filters_Product):
    template_name = 'product/filter_product.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Filters_Product_Liked_Product, self).get_context_data(*args, **kwargs)
        name_filter = self.kwargs['filter']
        context['now_categ'] = self.kwargs['url_name']

        if name_filter not in ['ascending', 'descending']:
            want_category = Category.objects.filter(name=name_filter).first()
            context['product'] = My_product.objects.filter(gender=self.kwargs['url_name'], categ=want_category.id)

        else:
            if name_filter=='ascending':
                context['product'] = My_product.objects.order_by('price')
            else:
                context['product'] = My_product.objects.order_by('-price')

        context['categ_product'] = Category.objects.all()
        context['menu'] = self.menu

        return context


class In_the_basket(TemplateView):

    template_name = 'person/in_basket.html'







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