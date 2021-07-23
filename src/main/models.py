import hashlib
from datetime import datetime

from django.db import models
from django.utils.timezone import now
from django.core.cache import cache

from main import choices


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    name = models.CharField('Имя автора', max_length=100, null=True)
    last_name = models.CharField('Фамилия автора', max_length=100, null=True)
    email = models.EmailField('Email автора', max_length=50, null=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'


class Subscriber(models.Model):
    class Meta:
        unique_together = ['email_to', 'author_id']

    email_to = models.EmailField('Email подписчика')
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.email_to

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     return super(Subscriber, self).save(*args, **kwargs)
    #
    # def clean(self):
    #     self.validate_unique()


class Post(models.Model):
    class Meta:
        db_table = 'tbl_post'

    MOOD_CHOICES = (
        (1, 'happy'),
        (2, 'sad'),
        (3, 'informative'),
        (4, 'business'),
    )

    title = models.CharField('Заголовок', max_length=140)
    description = models.TextField('Краткое описание')
    content = models.TextField('Статья')
    mood = models.PositiveSmallIntegerField(choices=MOOD_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.title} - {self.created}'

    # def save(self):
    #     super(self).save()
    #     key = self.__class__.cache_key()
    #     cache.delete(key)

    @classmethod
    def cache_key(cls):
        dt = datetime.today().strftime("%Y-%m-%d")
        key = f'post_all_{dt}'
        return key


# class Metrika(models.Model):
#     utm = models.CharField('utm metka', max_length=50)
#     time_exec = models.CharField('time execution')
#     created = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=250)
    # author = models.ForeignKey('Author', models.CASCADE, default=None)
    author = models.ForeignKey(Author, models.CASCADE, related_name='books')

    def __str__(self):
        return 'book: id: {}, title: {}, author: {}'.format(self.id, self.title, self.author)


class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()


class Rate(models.Model):
    currency = models.PositiveSmallIntegerField(choices=choices.CURRENCY_CHOICES, db_index=True)
    source = models.PositiveSmallIntegerField(choices=choices.SOURCE_CHOICES)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("rate_edit_all____2", "-------- edit all fields")
        ]

    def __str__(self):
        return 'sale: {}, buy: {}, source: {}'.format(self.buy, self.buy, self.get_source_display)


class URLTracker(models.Model):
    path = models.CharField(max_length=256, unique=True)
    counter = models.PositiveBigIntegerField()

    def __str__(self):
        return f'ID: {self.id}; path: {self.path}; counter: {self.counter}'

