from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    """Manager for users"""
    def create_user(self, email, password = None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

