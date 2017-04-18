# coding=utf-8
from django.conf.urls import patterns, url

from .views import TicketView

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', TicketView.as_view(), name='send'),
)
