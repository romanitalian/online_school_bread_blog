# Generated by Django 3.2.4 on 2021-06-17 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_rate_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rate',
            options={'permissions': [('rate_edit_all____2', '-------- edit all fields')]},
        ),
    ]
