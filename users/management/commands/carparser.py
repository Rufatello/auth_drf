import requests
from django.core.management import BaseCommand

from auto.models import Brand


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://cars-base.ru/api/cars"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for i in data:
                Brand.objects.create(
                    make=i.get("name"),
                )
