from django.contrib import admin

from apps.main.models import Settings


@admin.register(Settings)
class TaskAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Settings._meta.fields]
