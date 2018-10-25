# Generated by Django 2.1 on 2018-10-15 07:25

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_comment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('comments', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
    ]
