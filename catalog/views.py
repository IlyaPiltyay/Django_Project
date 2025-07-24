from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.core.cache import cache

from catalog.services import get_products_by_category


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
        # Получаем category_id из параметров URL
        category_id = self.kwargs.get('category_id')

        # Формируем ключ кэша для списка продуктов в определённой категории
        cache_key = f'product_queryset_category_{category_id}'

        # Пытаемся получить закешированный queryset
        queryset = cache.get(cache_key)

        if queryset is None:  # Если нет закешированного значения
            queryset = get_products_by_category(category_id)
            cache.set(cache_key, queryset, 60 * 15)  # Кешируем queryset на 15 минут

        return queryset

    @staticmethod
    def clear_category_cache(category_id):
        """ Очищает кэш для данной категории. """
        cache_key = f'product_queryset_category_{category_id}'
        cache.delete(cache_key)
        print(f"Кэш для категории {category_id} очищен.")


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

    def get_success_url(self):
        category_id = self.object.category.id  # Получаем id категории для кэша
        ProductListView.clear_category_cache(category_id)
        return super().get_success_url()


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'products'
