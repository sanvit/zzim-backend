from django.db import models
import uuid
from user.models import User
# Create your models here.


class item(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False, null=False, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False, default=0)
    shipping = models.PositiveIntegerField(null=False, blank=False, default=0)
    mall = models.ForeignKey("shoppingMall", on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=False, blank=False)
    item_no = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)
    is_purchased = models.BooleanField(default=False, null=False, blank=False)
    is_shared = models.BooleanField(default=False, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.name}"


class shoppingMall(models.Model):
    url = models.URLField(null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=100, null=False, blank=False)
    icon = models.URLField(null=False, blank=False)
    logo = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.name
