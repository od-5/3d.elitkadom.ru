# coding=utf-8
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.conf import settings

from apps.landing.models import Setup
from .forms import TicketForm


__author__ = 'alexy'


def ticket_send(request):
    try:
        email = Setup.objects.all().first().email
        if not email:
            email = 'od-5@yandex.ru'
    except:
        email = 'od-5@yandex.ru'
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.save()
            mail_theme_msg = u'3d.elitkadom.ru - %s' % ticket.theme
            message = u'Тема: %s\nДома: %s\nТелефон или e-mail: %s\n' % \
                      (ticket.theme, ticket.house, ticket.phone)
            send_mail(
                mail_theme_msg,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )

    return HttpResponseRedirect(reverse('landing:ok'))