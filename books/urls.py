from django.urls import path, include

from . import views


app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book', views.add_book, name='addbook'),
    path('book/<int:book_id>', views.detail_book, name='detail'),
    path('<int:book_id>/recommend',views.recommend_book,name="recommend"),
    path('search',views.search,name="search"),
    path('category/<category>',views.category,name="category"),
    path('author/<author>',views.author,name="author"),
    path('download/<book>/',views.download_book,name="download"),




]