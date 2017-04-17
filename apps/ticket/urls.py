# coding=utf-8
from django.conf.urls import patterns, url

from .views import ticket_send

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ticket_send, name='send'),
)
