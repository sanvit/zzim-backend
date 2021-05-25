from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, password, nickname):
        user = self.model(nickname=nickname, username=username)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, username, password):
        user = self.model(nickname=nickname, username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    """ User Model """

    objects = UserManager()

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False,
                            blank=False, auto_created=True, editable=False)
    username = models.CharField(max_length=64, unique=True)
    nickname = models.CharField(max_length=64, null=False, blank=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname"]
