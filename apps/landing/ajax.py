# coding=utf-8
import urllib
import urlparse
import urllib2
import json

from annoying.decorators import ajax_request
from annoying.functions import get_object_or_None

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from core.models import Setup

from .models import City

__author__ = 'alexy'


@ajax_request
@csrf_exempt
def ticket(request):
    name = request.POST.get('name') or ''
    phone = request.POST.get('phone') or ''
    mail = request.POST.get('mail') or ''
    theme = request.POST.get('theme') or ''
    city = request.POST.get('city') or ''
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
    values = {
        'name': name.encode('utf-8'),
        'phone': phone.encode('utf-8'),
        'mail': mail.encode('utf-8'),
        'theme': theme.encode('utf-8'),
        'city': city.encode('utf-8')
    }
    data = urllib.urlencode(values)
    req = urllib2.Request('http://reklamadoma.com/ticket/hanger/', data, headers)
    response = urllib2.urlopen(req)
    answer = json.load(response)
    if answer['success']:
        if mail:
            current_city = get_object_or_None(City, name=city)
            if current_city:
                price = current_city.price or '35 000'
                count = current_city.count or '50 000'
                if current_city.phone:
                    phone = current_city.phone
                else:
                    if Setup.object.first().phone:
                        phone = Setup.object.first().phone
                    else:
                        phone = None
                subject = u'Спасибо за заявку на сайте hanger-reklama.com'
                # msg_plain = render_to_string('email.txt', {'name': name})
                msg_html = render_to_string('landing/mail.html', {'phone': phone, 'price': price, 'count': count})
                # try:
                send_mail(
                    subject,
                    msg_html,
                    settings.DEFAULT_FROM_EMAIL,
                    [mail, ],
                    html_message=msg_html,
                )
                # except:
                #     pass
        return {
            'success': True,
            'name': name,
            'phone': phone,
            'mail': mail,
            'theme': theme
        }
    return {
        'success': False
    }
