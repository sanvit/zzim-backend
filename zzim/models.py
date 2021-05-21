from django.db import models
import uuid
# Create your models here.


class item(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False, null=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False, default=0)
    shipping = models.PositiveIntegerField(null=False, blank=False, default=0)
    mall = models.ForeignKey("shoppingMall", on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    is_purchased = models.BooleanField(default=False, null=False, blank=False)
    is_shared = models.BooleanField(default=False, null=False, blank=False)


class shoppingMall(models.Model):
    url = models.URLField(null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=100, null=False, blank=False)
    icon = models.URLField(null=False, blank=False)
    logo = models.URLField(null=False, blank=False)
