import os
from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Gender(models.Model):
    name = models.CharField('Nombre', max_length=50)

    categories = models.Manager()

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Nombre', max_length=50)

    authors = models.Manager()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Nombre', max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    description = models.TextField('Descripcion', null=False)
    gender = models.ManyToManyField(Gender)
    amount_pages = models.IntegerField('Cantidad de paginas')
    amount_chapter = models.IntegerField('Cantidad de capitulos')
    pub_date = models.DateTimeField(auto_now_add=True)
    recommended = models.IntegerField('Veces Recomendado', default=0)
    # content_adult = models.BooleanField('Solo para adultos?', default=1)
    public = models.BooleanField('Publico', default=0)
    file_book = models.FileField(verbose_name='Libro', upload_to='', default="")
    img_book = models.ImageField(verbose_name='Foto Portada', upload_to='', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="")

    books = models.Manager()  # The default manager.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"


class Comment(models.Model):
    text = models.TextField(verbose_name='Comentario', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, default="")
    datetime = models.DateTimeField(auto_now_add=True)


    comments = models.Manager()

    def get_comment_book(book_id):
        return models.Manager().filter(book_id=book_id)

    def __str__(self):
        return self.text
"""
class Download(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="")
    datetime = models.DateTimeField(auto_now_add=True)


"""