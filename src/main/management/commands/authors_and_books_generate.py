from faker import Faker
import random

from main.models import Author
from main.models import Book

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'generate random data'  # noqa

    def handle(self, *args, **options):
        Author.objects.all().delete()
        fake = Faker()
        for _ in range(1_000):
            try:
                Author(name=fake.name(), email=fake.email(), age=random.randint(1, 100)).save()
            except IntegrityError:
                pass
        for i in range(1_000):
            author = Author.objects.order_by('?').last()
            Book(title=f'Title {i}', author=author).save()
