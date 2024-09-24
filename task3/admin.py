from django.contrib import admin

from task3.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass