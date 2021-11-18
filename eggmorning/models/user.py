from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, phone, gender, birth, password=None):
        if not email:
            raise ValueError('must have user id')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            phone=phone,
            gender=gender,
            birth=birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password,
            gender="",
            phone="",
            birth=datetime.now()
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(max_length=255, default='', unique=True)
    nickname = models.CharField(max_length=32, default='', null=False, unique=True)
    phone = models.CharField(max_length=32, default='')
    gender = models.CharField(max_length=1, default='')
    birth = models.DateField(default='', blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

