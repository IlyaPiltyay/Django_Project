from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from catalog.models import Product


# Create your views here.

class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class CatalogView(ListView):
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'  # имя, с которым мы будем ссылаться на продукты в шаблоне

    def get_queryset(self):
        return Product.objects.all()  # Возвращает все продукты

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        products_by_category = {}

        for product in products:
            category = product.category.name
            if category not in products_by_category:
                products_by_category[category] = []
            products_by_category[category].append(product)

        context['products_by_category'] = products_by_category
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'  # Вы сможете ссылаться на продукт в шаблоне через 'product'

    def get_object(self):
        # Вызываем get_object из родительского класса, чтобы получить продукт по ID
        return get_object_or_404(Product, id=self.kwargs['id'])
