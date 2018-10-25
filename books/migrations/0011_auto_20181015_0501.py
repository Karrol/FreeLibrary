# Generated by Django 2.1 on 2018-10-15 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20181015_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file_book',
            field=models.FileField(default='', upload_to='books/book', verbose_name='Libro'),
        ),
        migrations.AlterField(
            model_name='book',
            name='img_book',
            field=models.ImageField(default='', upload_to='books/cover', verbose_name='Foto Portada'),
        ),
    ]