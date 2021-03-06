# coding=utf-8
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from apps.landing.models import Setup
from .models import Ticket


__author__ = 'alexy'


class TicketView(CreateView):
    model = Ticket
    fields = ['phone', 'name', 'theme', 'city']
    success_url = reverse_lazy('landing:ok')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TicketView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.status = 1
        # house = form.cleaned_data.get('house')
        phone = form.cleaned_data.get('phone')
        theme = form.cleaned_data.get('theme')
        name = form.cleaned_data.get('name')
        city = form.cleaned_data.get('city' or None)
        if city and city.email:
            email = city.email
        else:
            setup = Setup.objects.all().first()
            if setup and setup.email:
                email = setup.email
            else:
                email = None
        if email:
            mail_theme_msg = u'3d.elitkadom.ru - %s' % theme
            message = u'Тема: %s\nТелефон: %s\nФИО: %s\n' % \
                      (theme, phone, name)
            send_mail(
                mail_theme_msg,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )
        return super(TicketView, self).form_valid(form)
