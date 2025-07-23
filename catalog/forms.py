from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'is_published']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Добавляем CSS классы
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену продукта'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})  # Для загрузки файла
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Проверка на наличие запрещенных слов
        for word in self.forbidden_words:
            if word in name.lower():
                raise forms.ValidationError(f"Название не должно содержать слово: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        # Проверка на наличие запрещенных слов
        for word in self.forbidden_words:
            if word in description.lower():
                raise forms.ValidationError(f"Описание не должно содержать слово: {word}")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        # Валидация цены на отрицательное значение
        if price is not None and price <= 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price


# class ProductModeratorForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         exclude = ('can_unpublish_product',)
