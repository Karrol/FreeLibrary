# Generated by Django 2.1 on 2018-10-14 07:33

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20181014_0109'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('books', django.db.models.manager.Manager()),
            ],
        ),
    ]
