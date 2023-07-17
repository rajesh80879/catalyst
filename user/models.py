from django.db.models import *
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from user.managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
   
    name = CharField(max_length=50)
    email = EmailField(unique=True)
    password = CharField(max_length=255, default="")

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.name
