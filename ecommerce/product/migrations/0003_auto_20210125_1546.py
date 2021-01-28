# Generated by Django 3.1.5 on 2021-01-25 10:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(150000)], verbose_name='Price'),
        ),
    ]
