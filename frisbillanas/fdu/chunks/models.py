from django.db import models
from django.utils.translation import ugettext_lazy as _

from transmeta import TransMeta


class HTMLChunk(models.Model):
    __metaclass__ = TransMeta

    code = models.SlugField(_('Code'))
    body = models.TextField(_('Body'), default='')

    class Meta:
        translate = ('body', )
