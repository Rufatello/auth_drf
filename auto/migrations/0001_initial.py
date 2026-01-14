

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("make", models.CharField(max_length=100, verbose_name="Марка")),
                ("model", models.CharField(max_length=100, verbose_name="Модель")),
            ],
            options={
                "verbose_name": "Марка и модель",
                "verbose_name_plural": "Марки и модели",
            },
        ),
    ]
