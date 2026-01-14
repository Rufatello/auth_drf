
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0006_alter_auto_options_auto_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="carbody",
            name="slug",
            field=models.SlugField(default=2, unique=True, verbose_name="Слаг"),
            preserve_default=False,
        ),
    ]
