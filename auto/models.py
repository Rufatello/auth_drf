from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime
from slugify import slugify

from auto.image_path import photo_auto
from users.models import User, NULLABLE


class Brand(models.Model):
    make = models.CharField(verbose_name="Марка", max_length=100)

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

    def __str__(self):
        return self.make


class CarBody(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    slug = models.SlugField(verbose_name="Слаг", unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Кузов"
        verbose_name_plural = "Кузова"

    def __str__(self):
        return self.name


class Auto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    make = models.ForeignKey(Brand, verbose_name="Марка", on_delete=models.CASCADE)
    years = models.PositiveIntegerField(
        verbose_name="Год выпуска",
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],
    )
    model = models.CharField(verbose_name="Модель", max_length=100)
    car_body = models.ForeignKey(
        CarBody, verbose_name="Кузов", on_delete=models.PROTECT
    )

    annotation = models.BooleanField(
        default=False, verbose_name="Аннотация", **NULLABLE
    )

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class AutoPhoto(models.Model):
    auto = models.ForeignKey(
        Auto, on_delete=models.CASCADE, verbose_name="Фото", related_name="photos"
    )
    photo = models.ImageField(upload_to=photo_auto, verbose_name="Фото")

    class Meta:
        verbose_name = "Фото_автомобиля"
        verbose_name_plural = "Фото_автомобилей"

    def __str__(self):
        return f"Фото {self.auto}"
