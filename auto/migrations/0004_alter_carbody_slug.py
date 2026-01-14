
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0003_carbody_alter_brand_options_auto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carbody",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
