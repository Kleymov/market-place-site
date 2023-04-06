from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django import forms

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, name, last_name, password, **kwargs):
        user = self.create_user(email, name, last_name, password, **kwargs)

        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user

    def create_user(self, email, name, last_name, password, **kwargs):
        email = self.normalize_email(email)

        user = self.model(email = email, name = name, last_name = last_name, **kwargs)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    name = models.CharField(verbose_name='Отображаемое имя', max_length=255, unique=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True, null=True, default='')
    cart = models.TextField(verbose_name='Корзина', blank=True, null=True,)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Доступ в админ панель', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomAccountManager()

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
       return self.is_staff

    def has_module_perms(self, app_label):
       return self.is_staff

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
