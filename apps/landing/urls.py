# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import LandingView, CityDetailView
from .ajax import city_map

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.landing.views',
    url(r'^$', LandingView.as_view(), name='index'),
    url(r'^ok/$', TemplateView.as_view(template_name='landing/ok.html'), name='ok'),
    url(r'^city_map/$', city_map, name='city-map'),
    url(r'^(?P<slug>[\w-]+)/$', CityDetailView.as_view(), name='city'),
    # url(r'^ticket/$', ticket, name='ticket'),
)
