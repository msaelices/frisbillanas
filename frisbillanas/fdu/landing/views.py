import json

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from chunks.models import HTMLChunk


def home(request):
    """ Home page """
    html_chunks = {}
    for chunk in HTMLChunk.objects.all():
        html_chunks[chunk.code] = mark_safe(chunk.body)

    return render(request, 'landing/home.html', {'html_chunks': html_chunks})


def send_message(request):
    """ contact view """
    contact_name = request.POST['contactName']
    contact_email = request.POST['email']
    body = request.POST['comments']
    send_mail('Mensaje de %s <%s> para Frisbillanas' % (contact_name, contact_email), body, contact_email,
    settings.ADMINS, fail_silently=False)    
    return HttpResponse(json.dumps({'result': 'ok'}), content_type="application/json")
