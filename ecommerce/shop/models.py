from django.db import models
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