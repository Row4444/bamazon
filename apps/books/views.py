from django.shortcuts import render

from django.views import generic

from apps.books.models import Book


class BooksListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book



