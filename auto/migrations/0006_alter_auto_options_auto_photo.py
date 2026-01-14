
import auto.image_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0005_remove_carbody_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="auto",
            options={"verbose_name": "Автомобиль", "verbose_name_plural": "Автомобили"},
        ),
        migrations.AddField(
            model_name="auto",
            name="photo",
            field=models.ImageField(
                default=2, upload_to=auto.image_path.photo_auto, verbose_name="фото"
            ),
            preserve_default=False,
        ),
    ]
