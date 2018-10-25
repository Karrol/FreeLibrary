import os


from django.core.paginator import Paginator
from django.db.models.functions import Coalesce, Lower
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from FreeLibrary import settings
from books.forms import AddBookForm
from .models import Book, Gender, Comment, Author


def index(request):
    book_list = Book.books.order_by(Lower('pub_date').desc()).filter(public=True)
    paginator = Paginator(book_list, 8)  # Show 8 book per page

    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {
        'books': books,
        'categories': Gender.categories.all(),
        'authors': Author.authors.all(),

    }

    return render(request, 'books/index.html', context)


@login_required
def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.user = request.user
            blog_item.save()

            return redirect('books:index')

    else:
        form = AddBookForm()
    return render(request, 'books/new.html', {'form': form})


@login_required
def download_book(request, book):
    file_path = os.path.join(settings.MEDIA_ROOT, book)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            # download = Download.objects.create(user=request.user)
            return response

    raise Http404


def search(request):
    q = request.GET.get('q', '')
    books = Book.books.filter(name__icontains=q)

    context = {
        'books': books,
        'categories': Gender.categories.all(),
        'authors': Author.authors.all(),
        'nofound': count_query(books),
    }
    return render(request, 'books/index.html', context)


def detail_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    return render(request, 'books/detail.html',
                  {'book': book, 'comments': Comment.comments.filter(book_id__exact=book_id)})


@login_required
def recommend_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.recommended = book.recommended + 1
    book.save()
    return HttpResponse("Tu has recomendado este libro %s." % book_id)


def category(request, category):
    books = Book.books.filter(gender__name__icontains=category)

    context = {
        'books': books,
        'categories': Gender.categories.all(),
        'authors': Author.authors.all(),
        'no_book_category': count_query(books)
    }
    return render(request, 'books/index.html', context)


def author(request, author):
    books = Book.books.filter(author__name__icontains=author)

    context = {
        'books': books,
        'categories': Gender.categories.all(),
        'authors': Author.authors.all(),
        'no_book_author': count_query(books)
    }
    return render(request, 'books/index.html', context)


def count_query(query):
    """"
    Vertifica que la query devuelva mas de un registro
    """
    result = False
    if query.count() < 1:
        result = True
    return result
