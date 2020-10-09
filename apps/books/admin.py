from django.contrib import admin

from apps.books.models import Book


@admin.register(Book)
class TaskAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]
