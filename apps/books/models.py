from django.db import models

from apps.authors.models import Author


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=128, verbose_name="Book's title", unique=True)
    cover = models.ImageField(verbose_name="Book's cover", upload_to="books/covers/", null=True, blank=True)

    def str(self):
        return self.title
