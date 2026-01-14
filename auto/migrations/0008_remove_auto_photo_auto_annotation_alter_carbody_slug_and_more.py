
import auto.image_path
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0007_carbody_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auto",
            name="photo",
        ),
        migrations.AddField(
            model_name="auto",
            name="annotation",
            field=models.BooleanField(default=False, verbose_name="Аннотация"),
        ),
        migrations.AlterField(
            model_name="carbody",
            name="slug",
            field=models.SlugField(blank=True, unique=True, verbose_name="Слаг"),
        ),
        migrations.CreateModel(
            name="AutoPhoto",
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
                    "photo",
                    models.ImageField(
                        upload_to=auto.image_path.photo_auto, verbose_name="Фото"
                    ),
                ),
                (
                    "auto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="auto.auto",
                        verbose_name="Фото",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото_автомобиля",
                "verbose_name_plural": "Фото_автомобилей",
            },
        ),
    ]
