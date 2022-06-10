from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.

class CustomManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_staff", True)

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser = True.")

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError("you must provide an email")
        
        if password and len(password) > 16:
            raise ValueError("password must be smaller than 16 characters")

        user = self.model(email = email, **other_fields)

        # user.set_password(validated_data['password'])
        user.set_password(password)
        user.save()
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=64)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["password"]

    def __str__(self):
        return self.email


class Books(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name