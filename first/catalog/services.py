from django.core.cache import cache
from .models import Category, Product


def get_products_from_cache():
    """Сервисный слой для получения кэша в ProductListView"""
    key = 'product_list'
    products_list_cache = cache.get(key)
    # Проверяю, получил ли я кэш
    if products_list_cache is not None:
        return products_list_cache
    # Если кэш не получен, то записываю его из БД для последующего использования
    else:
        products = Product.objects.all()
        cache.set(products, key)
        return products


def get_categories_from_cache():
    """Получаем категории из кэша, если кэш пуст, получаем данные из БД."""
    key = "categories_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
