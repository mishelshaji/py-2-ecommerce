from django.db import models
from django.core import validators
import uuid

# Create your models here.
class Brand(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name=models.CharField(
        max_length=50,
        verbose_name='Brand Name',
        unique=True
    )

    description=models.TextField(
        max_length=500,
        verbose_name='Description'
    )

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name=models.CharField(
        max_length=50,
        verbose_name='Category Name',
        unique=True
    )

    description=models.TextField(
        max_length=500,
        verbose_name='Description'
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name=models.CharField(
        max_length=100,
        verbose_name='Product Name',
        unique=True
    )

    description=models.TextField(
        max_length=500,
        verbose_name='Description'
    )

    stock = models.IntegerField(
        verbose_name='Stock',
        validators=[
            validators.MinValueValidator(10),
            validators.MaxValueValidator(10000),
        ]
    )

    price = models.FloatField(
        verbose_name='Price',
        default=0,
        validators=[
            validators.MinValueValidator(10),
            validators.MaxValueValidator(150000),
        ]
    )

    image = models.ImageField(
        verbose_name='Product Image',
        upload_to='product/images/'
    )

    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name