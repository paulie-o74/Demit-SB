from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Admin for products
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'is_original',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin for categories
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
