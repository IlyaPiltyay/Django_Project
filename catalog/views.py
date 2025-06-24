from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def catalog(request):
    products = Product.objects.all()
    products_by_category = {}

    for product in products:
        category = product.category.name
        if category not in products_by_category:
            products_by_category[category] = []
        products_by_category[category].append(product)

    context = {"products_by_category": products_by_category}
    return render(request, 'catalog/catalog.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)  # Получаем товар по ID
    context = {
        "product": product,  # Передаем продукт в контекст
    }
    return render(request, 'catalog/product_detail.html', context)
