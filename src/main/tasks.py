import requests
from celery import shared_task
from time import sleep
from decimal import Decimal

from main.models import Rate
from main.notify_service import notify


@shared_task
def smth_slow_async(wait=10):
    sleep(wait)


@shared_task
def subscribe_notify(email_to, author_name):
    sleep(10)
    notify(email_to, author_name)


@shared_task
def parse_privatbank():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)

    # raise error if response.status_code != 200
    response.raise_for_status()

    data = response.json()
    source = 1
    currency_map = {
        'USD': 1,
        'EUR': 2,
    }

    TWOPLACES = Decimal(10) ** -2

    for row in data:
        if row['ccy'] in currency_map:
            buy = Decimal(row['buy']).quantize(TWOPLACES)
            sale = Decimal(row['sale']).quantize(TWOPLACES)
            currency = currency_map[row['ccy']]

            last_rate = Rate.objects.filter(source=source, currency=currency).last()
            # save rate if record was not found or sale or buy was changed
            if last_rate is None or buy != last_rate.buy or sale != last_rate.sale:
                Rate.objects.create(
                    currency=currency,
                    source=source,
                    sale=sale,
                    buy=buy,
                )
