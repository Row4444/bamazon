from django.views import generic

from apps.authors.models import Author


class AuthorDetailView(generic.DetailView):
    model = Author
