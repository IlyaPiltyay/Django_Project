from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.contrib import messages


# Create your views here.

class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class CatalogView(ListView):
    model = Category
    template_name = 'catalog/catalog.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')  # Получаем category_id из URL
        return Product.objects.filter(category_id=category_id, is_published=True)  # Фильтруем продукты по категории


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        # Устанавливаем владельца продукта на текущего пользователя
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        product = self.get_object()
        # Проверка на право изменения статуса публикации
        if 'is_published' in form.changed_data:
            if not self.request.user.has_perm('catalog.can_unpublish_product') and product.owner != self.request.user:
                raise PermissionDenied(
                    "У вас нет прав на отмену публикации продукта или вы не являетесь владельцем продукта.")
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # Проверка прав: только владелец или модератор могут редактировать продукт
        if not (request.user == product.owner or request.user.groups.filter(name='moderator').exists()):
            raise PermissionDenied("У вас нет прав для редактирования данного продукта.")

        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:catalog')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # Проверка прав: только владелец или модератор могут удалить продукт
        if not (request.user == product.owner or request.user.groups.filter(name='moderator').exists()):
            raise PermissionDenied("У вас нет прав для удаления данного продукта.")

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Продукт "{self.get_object().name}" был успешно удалён.')
        return super().delete(request, *args, **kwargs)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'products'
