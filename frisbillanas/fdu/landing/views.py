from django.shortcuts import render
from django.utils.safestring import mark_safe

from chunks.models import HTMLChunk


def home(request):
    """ Home page """
    html_chunks = {}
    for chunk in HTMLChunk.objects.all():
        html_chunks[chunk.code] = mark_safe(chunk.body)

    return render(request, 'landing/home.html', {'html_chunks': html_chunks})
