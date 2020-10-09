from django.shortcuts import render

from apps.main.models import Settings


def index(request):
    index_text = Settings.objects.filter(pk=1).first()
    return render(request, 'main/index.html', {'index_text': index_text})