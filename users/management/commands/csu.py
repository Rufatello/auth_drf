from django.core.management import BaseCommand
from dotenv import load_dotenv
from users.models import User
import os

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv("EMAIL"),
            first_name=os.getenv("FIRST_NAME"),
            last_name=os.getenv("LAST_NAME"),
            surname=os.getenv("SURNAME"),
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv("SUPERUSER_PASSWORD"))
        user.save()
