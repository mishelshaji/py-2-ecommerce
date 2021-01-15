from django.db import models

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