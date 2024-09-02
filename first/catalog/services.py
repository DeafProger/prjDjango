from django.core.cache import cache
from .models import Product


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
