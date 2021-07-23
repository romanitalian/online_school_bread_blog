# Generated by Django 2.2.16 on 2021-05-13 02:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Имя автора')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Фамилия автора')),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='Email автора')),
                ('age', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('content', models.TextField(verbose_name='Статья')),
                ('mood', models.PositiveSmallIntegerField(choices=[(1, 'happy'), (2, 'sad'), (3, 'informative'), (4, 'business')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'tbl_post',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='main.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.EmailField(max_length=254, verbose_name='Email подписчика')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Author')),
            ],
            options={
                'unique_together': {('email_to', 'author_id')},
            },
        ),
    ]