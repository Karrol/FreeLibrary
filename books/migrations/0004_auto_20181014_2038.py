# Generated by Django 2.1 on 2018-10-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20181014_0733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='gender',
        ),
        migrations.AddField(
            model_name='book',
            name='gender',
            field=models.ManyToManyField(to='books.Gender'),
        ),
    ]