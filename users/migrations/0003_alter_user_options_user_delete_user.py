from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_username_user_surname_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="delete_user",
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
