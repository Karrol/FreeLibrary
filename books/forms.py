from django import forms
from django.forms import ModelForm, Textarea, Select, SelectMultiple, CheckboxInput, FileInput
from django.forms.widgets import Input
from easy_select2 import select2_modelform_meta, select2_modelform

from books.models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = (
            'name', 'description', 'author', 'gender', 'amount_pages', 'amount_chapter',
            'img_book', 'file_book')

        labels = {
            'name': ('Nombre'),
        }

        widgets = {
            'name': Input(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'author': Select(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'gender': SelectMultiple(attrs={'class': 'form-control'}),
            'amount_pages': Input(attrs={'class': 'form-control'}),
            'amount_chapter': Input(attrs={'class': 'form-control'}),
            'content_adult': Input(attrs={'class': 'form-control'}),
            'img_book': FileInput(attrs={'class': 'form-control'}),
            'file_book': FileInput(attrs={'class': 'form-control'}),
        }
