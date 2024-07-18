from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price'),
    list_filter = ('category',),
    search_fields = ('name', 'description',)


admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
