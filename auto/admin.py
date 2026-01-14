from django.contrib import admin

from auto.models import Brand, Auto, CarBody


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("make",)


@admin.register(CarBody)
class CarBodyAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = (
        "make",
        "user",
        "years",
        "model",
        "car_body",
    )
