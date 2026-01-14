
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0002_alter_brand_options_remove_brand_model"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CarBody",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("slug", models.CharField(unique=True)),
            ],
            options={
                "verbose_name": "Кузов",
                "verbose_name_plural": "Кузова",
            },
        ),
        migrations.AlterModelOptions(
            name="brand",
            options={"verbose_name": "Марка", "verbose_name_plural": "Марки"},
        ),
        migrations.CreateModel(
            name="Auto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "years",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2026),
                        ],
                        verbose_name="Год выпуска",
                    ),
                ),
                ("model", models.CharField(max_length=100, verbose_name="Модель")),
                (
                    "make",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auto.brand",
                        verbose_name="Марка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
                (
                    "car_body",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="auto.carbody",
                        verbose_name="Кузов",
                    ),
                ),
            ],
        ),
    ]
