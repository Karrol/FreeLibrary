from django.contrib import admin
from easy_select2 import select2_modelform

from .models import *


# Register your models here.


BookForm = select2_modelform(Book, attrs={'width': '250px'})

def make_published(modeladmin, request, queryset):
    queryset.update(public=True)


def make_unpublished(modeladmin, request, queryset):
    queryset.update(public=False)


class BooksAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('name', 'author', 'amount_pages', 'amount_chapter', 'public')
    list_filter = ['pub_date', 'public']
    exclude = ['recommended']
    search_fields = ['name']
    actions = [make_published, make_unpublished]
    """"
    fieldsets = [
        ('Informacion del libro', {'fields': ['name','description','author','gender','amount_pages','amount_chapter','upload']}),
    ]
    """


admin.site.register(Book, BooksAdmin)
admin.site.register(Gender)
admin.site.register(Author)
admin.site.register(Comment)
# admin.site.register(Download)
