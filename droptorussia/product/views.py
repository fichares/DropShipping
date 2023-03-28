from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, My_product



class DataMixin:
    menu = [{'Men': "men"},  # title, url_name
            {'Women': "women"},
            {'Kids': "kids"}
            ]


class Page_Home(DataMixin, TemplateView):

    template_name = 'product/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu
        return context


class Choose_Product(DataMixin, TemplateView):

    template_name = 'product/choose_product.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Choose_Product, self).get_context_data(*args, **kwargs)
        context['product'] = My_product.objects.all()
        context['categ_product'] = Category.objects.all()
        context['menu'] = self.menu
        context['now_categ'] = self.kwargs['url_name']
        return context


