import requests
from bs4 import BeautifulSoup, Tag
from faker import Faker
import random

from main.models import Post, Author

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'parse and fill posts'  # noqa

    def handle(self, *args, **options):
        url = 'https://doroshenkoaa.ru/med/'
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        article_list = soup.find_all("a", {"class": "more"})
        for art in article_list:
            page_url = art.get('href')
            article_page = requests.get(page_url)
            soup_page = BeautifulSoup(article_page.content, 'html.parser')
            article_body = soup_page.find("div", {"itemprop": "articleBody"})
            article_title = soup_page.find("h1", {"itemprop": "headline"})

            Post(
                title=article_title.text.strip(),
                description=article_title.text,
                content=article_body.text,
            ).save(self)
