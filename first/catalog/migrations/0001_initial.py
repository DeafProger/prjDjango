# Generated by Django 5.0.7 on 2024-07-17 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование категории товара', max_length=255, verbose_name='Наименование категории')),
                ('description', models.TextField(help_text='Введите описание продукта', max_length=1023, verbose_name='Описание продукта')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование продукта', max_length=255, verbose_name='Наименование продукта')),
                ('description', models.TextField(help_text='Введите описание продукта', max_length=1023, verbose_name='Описание продукта')),
                ('image', models.ImageField(blank=True, help_text='Загрузите фото', null=True, upload_to='photo/product', verbose_name='Фото продукта')),
                ('price', models.PositiveIntegerField(help_text='Введите цену продукта', verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания записи в БД')),
                ('updated_at', models.DateTimeField(verbose_name='Дата последнего изменения записи в БД')),
                ('category', models.ForeignKey(help_text='Введите категорию товара', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
