from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm
from catalog.models import Product

# Create your views here.

class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class CatalogView(ListView):
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'

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


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
