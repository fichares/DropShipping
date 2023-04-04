from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
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
        context['product'] = My_product.objects.filter(gender=self.kwargs['url_name'])
        context['categ_product'] = Category.objects.all()
        context['menu'] = self.menu
        context['now_categ'] = self.kwargs['url_name']
        return context


class Filters_Product(Choose_Product):
    template_name = 'product/filter_product.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Filters_Product, self).get_context_data(*args, **kwargs)
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


class Product_View(DataMixin, ListView):
    model = My_product
    template_name = 'product/product_view.html'
 #   def get_object(self, queryset=None):
 #       now_url_name_product = self.kwargs['url_product_name']
 #       objekt = My_product.objects.get(url_name=now_url_name_product)
 #       return objekt

    def get_context_data(self, **kwargs):
        context = super(Product_View, self).get_context_data(**kwargs)
        context['categ_product'] = Category.objects.all()
        context['menu'] = self.menu
        context['now_categ'] = self.kwargs['url_name']
        now_url_name_product = self.kwargs['url_product_name']
        context['now_my_product'] = My_product.objects.get(url_name=now_url_name_product)
        return context