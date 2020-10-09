from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.books import views as books_view
from apps.authors import views as authors_view
from apps.main import views as main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view.index, name='index'),
    path('books/<int:pk>/', books_view.BookDetailView.as_view(), name='book_detail'),
    path('books/', books_view.BooksListView.as_view(), name='books_list'),
    path('author/<int:pk>/', authors_view.AuthorDetailView.as_view(), name='author_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
