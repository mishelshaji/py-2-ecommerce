from django.db import models
from django.db.models.base import ModelState
from product.models import Product
from accounts.models import User
import uuid

# Create your models here.
class Cart(models.Model):
    class Meta:
        unique_together = ['product', 'user']

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    session_id = models.CharField(
        max_length=100,
    )

    intent_id = models.CharField(
        max_length=100,
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )

    is_success = models.BooleanField(
        default=False,
        verbose_name='Payment Status'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    transaction_id = models.UUIDField(
        verbose_name='Transaction Id'
    )

class PurchasedProducts(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE
    )

    purchase_date = models.DateTimeField(
        auto_now_add=True
    )