from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', blank=False, null=False, unique=True)


def user_ava_upload(instance, filename):
    return f'{instance.user_id}/{filename}'


class Ava(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to=user_ava_upload)
    is_active = models.BooleanField(default=False)
