import json
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.utils import timezone

from chunks.models import HTMLChunk


def home(request):
    """ Home page """
    html_chunks = {}

    now = timezone.now()
    chiripones_registration_start = timezone.datetime(
        year=now.year,
        month=settings.CHIRIPONES_REGISTRATION_DATE[0],
        day=settings.CHIRIPONES_REGISTRATION_DATE[1],
        tzinfo=now.tzinfo,
    )
    chiripones_registration_end = chiripones_registration_start + timedelta(days=31)

    show_chiripones = chiripones_registration_end > now > chiripones_registration_start \
        or 'show_chiripones' in request.GET

    for chunk in HTMLChunk.objects.all():
        html_chunks[chunk.code] = mark_safe(chunk.body)

    return render(request, 'landing/home.html', {
        'html_chunks': html_chunks,
        'show_chiripones': show_chiripones,
    })


def send_message(request):
    """ contact view """
    contact_name = request.POST['contactName']
    contact_email = request.POST['email']
    body = request.POST['comments']
    send_mail('Mensaje de %s <%s> para Frisbillanas' % (contact_name, contact_email), body, contact_email,
    settings.ADMINS, fail_silently=False)
    return HttpResponse(json.dumps({'result': 'ok'}), content_type="application/json")
