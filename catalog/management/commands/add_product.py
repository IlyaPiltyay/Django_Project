from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test product to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name='Товары', description='Товары Тест')

        productsss = [
            {'name': 'Машина', 'description': 'авто', 'price': 12, 'category': category},
            {'name': 'Телефон', 'description': 'техника', 'price': 12, 'category': category},
        ]

        for product_data in productsss:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'product already exists: {product.name}'))
