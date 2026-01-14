from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    ROLE = (("admin", "Admin"), ("user", "User"))
    username = None
    email = models.EmailField(verbose_name="Почта", unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    surname = models.CharField(verbose_name="Отчество", max_length=50, **NULLABLE)
    is_active = models.BooleanField(verbose_name="Активность", default=True)
    delete_user = models.DateField(auto_now=True, **NULLABLE)
    role = models.CharField(choices=ROLE, default="user")
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
