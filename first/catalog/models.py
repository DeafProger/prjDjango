from django.db import models
from users.models import User


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
        auto_now_add=True,
        verbose_name='Дата создания записи в БД'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
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
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        null=True, blank=True,
        related_name='users',  # "products",
    )


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
        help_text="Выберите продукт",
    )
    version_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
    )
    version_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    is_version_active = models.BooleanField(
        default=False,
        verbose_name="Активная версия",
        help_text="Является ли версия активной?",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name
