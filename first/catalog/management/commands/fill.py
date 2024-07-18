import json

from django.core.management import BaseCommand

from ...models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_catalog():
        with open('catalog_data.json', 'r', encoding='utf-8') as file:
            catalog = json.load(file)
        return catalog

    def handle(self, *args, **options):
        # Удаляем все продукты из базы данных
        Product.objects.all().delete()
        # Удаляем все категории из базы данных
        Category.objects.all().delete()

        for item in Command.json_read_catalog():
            if item["model"] == 'catalog.category':
                Category.objects.create(
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    id=item['pk'],
                )
            else:
                Product.objects.create(
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    price=item['fields']['price'],
                    image=item['fields']['image'],
                    created_at=item['fields']['created_at'],
                    updated_at=item['fields']['updated_at'],
                    id=item['pk'],
                    category_id=item['fields']['category'],
                )
