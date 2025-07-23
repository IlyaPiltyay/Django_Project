from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fields = ('email', 'first_name', 'last_name', 'avatar', 'phone_number', 'country','groups')
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
