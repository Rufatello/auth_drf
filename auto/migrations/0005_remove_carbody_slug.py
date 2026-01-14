
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auto", "0004_alter_carbody_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carbody",
            name="slug",
        ),
    ]
