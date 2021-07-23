import decimal
import random
from django.core.management.base import BaseCommand

from main.models import Rate
from main.tasks import parse_privatbank


class Command(BaseCommand):
    help = 'generate random Rates'  # noqa

    def handle(self, *args, **options):
        # parse_privatbank()
        for _ in range(1000):
            Rate.objects.create(
                currency=random.randint(1, 2),
                source=random.randint(1, 3),
                sale=decimal.Decimal(random.randrange(20, 50)),
                buy=decimal.Decimal(random.randrange(20, 50)),
            )
        print(f'rates count: {Rate.objects.count()}')

