''' Register Products and Category for admin '''
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    ''' Register Product Model'''
    list_display = (
        'sku',
        'name',
        'price',
        'image',
        'category',
    )
    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    ''' Register Category Model'''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
