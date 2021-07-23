import requests
from bs4 import BeautifulSoup, Tag
from faker import Faker
import random

from main.models import Post, Author

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'parse and fill posts'  # noqa

    def handle(self, *args, **options):
        from django.db import transaction
        with transaction.atomic():
            # user-1
            Post(
                title='tile-1',
                description='description-1',
                content='content-1',
            ).save(self)

            1 + '1'

            # user-2
            Post(
                title='tile-2',
                description='description-2',
                content='content-2',
            ).save(self)
