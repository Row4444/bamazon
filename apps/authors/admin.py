from django.contrib import admin

from apps.authors.models import Author


@admin.register(Author)
class TaskAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Author._meta.fields]
