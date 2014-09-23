from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import HTMLChunk


class HTMLChunkAdmin(SummernoteModelAdmin):
    pass


admin.site.register(HTMLChunk, HTMLChunkAdmin)