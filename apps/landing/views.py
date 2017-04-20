# coding=utf-8
from annoying.functions import get_object_or_None
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import ContextMixin

from .models import Setup, City, Video, Why, Service, Review, Thanks, Gallery, Client, Cost

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
            'cost_list': Cost.objects.all(),
            'client_list': Client.objects.all(),
            'gallery_list': Gallery.objects.all(),
            'thanks_list': Thanks.objects.all(),
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
        kwargs.update({
            'SETUP': Setup.objects.first(),
        })
        return kwargs


class LandingView(TemplateView, LandingMixin, SetupMixin):
    template_name = 'landing/index.html'


class CityDetailView(DetailView, LandingMixin, SetupMixin):
    model = City
    template_name = 'landing/index.html'
