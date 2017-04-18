# coding=utf-8
from annoying.functions import get_object_or_None
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import ContextMixin

from .models import Setup, City, Video, Why, Service, Review

__author__ = 'alexy'


class LandingMixin(ContextMixin):
    """
    Миксин добавляет в контекст:
    список городов
    список видео

    """
    def get_context_data(self, **kwargs):
        kwargs = super(LandingMixin, self).get_context_data(**kwargs)
        kwargs.update({
            'city_list': City.objects.all(),
            'review_list': Review.objects.all(),
            'service_list': Service.objects.all(),
            'why_list': Why.objects.all(),
            'video_list': Video.objects.all(),
            'main_video': get_object_or_None(Video, main=True)
        })
        return kwargs


class SetupMixin(ContextMixin):
    """
    Миксин добавляет сео настройки
    """
    def get_context_data(self, **kwargs):
        kwargs = super(SetupMixin, self).get_context_data(**kwargs)
        setup = Setup.objects.first()
        contact = phone = meta_title = meta_key = meta_desc = top_js = bottom_js = ''
        if setup:
            contact = setup.contact
            phone = setup.phone
            meta_title = setup.meta_title
            meta_key = setup.meta_key
            meta_desc = setup.meta_desc
            top_js = setup.top_js
            bottom_js = setup.bottom_js
        kwargs.update({
            'CONTACT': contact,
            'PHONE': phone,
            'TITLE': meta_title,
            'KEYS': meta_key,
            'DESC': meta_desc,
            'TOP_JS': top_js,
            'BOTTOM_JS': bottom_js
        })
        return kwargs


class LandingView(TemplateView, LandingMixin, SetupMixin):
    template_name = 'landing/index.html'


class CityDetailView(DetailView, LandingMixin, SetupMixin):
    model = City
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        kwargs = super(CityDetailView, self).get_context_data(**kwargs)
        if self.object.phone:
            kwargs['PHONE'] = self.object.phone
        if self.object.meta_title:
            kwargs['TITLE'] = self.object.meta_title
        if self.object.meta_key:
            kwargs['KEYS'] = self.object.meta_key
        if self.object.meta_desc:
            kwargs['DESC'] = self.object.meta_desc
        if self.object.contact:
            kwargs['CONTACT'] = self.object.contact
        return kwargs
