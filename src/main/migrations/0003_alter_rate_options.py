# Generated by Django 3.2.4 on 2021-06-17 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rate',
            options={'permissions': [('change_values', 'Can change values: buy and sale')]},
        ),
    ]