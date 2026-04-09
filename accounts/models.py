from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "customers"
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
