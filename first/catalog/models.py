from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование категории',
        help_text='Введите наименование категории товара'
    )
    description = models.TextField(
        max_length=1023,
        verbose_name='Описание продукта',
        help_text='Введите описание продукта'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name='Наименование продукта',
        help_text='Введите наименование продукта'
    )
    description = models.TextField(
        max_length=1023,
        verbose_name='Описание продукта',
        help_text='Введите описание продукта'
    )
    image = models.ImageField(
        upload_to='photo/product',
        blank=True,
        null=True,
        verbose_name='Фото продукта',
        help_text='Загрузите фото'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Введите категорию товара'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена за покупку',
        help_text='Введите цену продукта'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания записи в БД'
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата последнего изменения записи в БД',
    )
    # uncomment and comment following lines for migration and back to 0001
    """
    manufactured_at = models.DateTimeField(
        verbose_name='Дата произодства',
        help_text='Введите дату производства продукта',
        null=True
    )
    """

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
