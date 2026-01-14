

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brand",
            options={"verbose_name": "Маркаь"},
        ),
        migrations.RemoveField(
            model_name="brand",
            name="model",
        ),
    ]
