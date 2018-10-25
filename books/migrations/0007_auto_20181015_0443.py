# Generated by Django 2.1 on 2018-10-15 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_content_adult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file_book',
            field=models.FileField(default='', upload_to='assets/uploads/books/book', verbose_name='Libro'),
        ),
        migrations.AlterField(
            model_name='book',
            name='img_book',
            field=models.ImageField(default='', upload_to='assets/uploads/books/cover', verbose_name='Foto Portada'),
        ),
    ]
