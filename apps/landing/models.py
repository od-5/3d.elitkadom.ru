# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

from core.base_model import CommonPage
from core.geotagging import geocode

__author__ = 'alexy'


class Setup(CommonPage):
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)
    robots_txt = models.TextField(verbose_name=u'ROBOTS.TXT', blank=True, null=True)
    sitemap = models.TextField(verbose_name=u'sitemap.xml', blank=True, null=True)

    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
        app_label = 'landing'


class City(CommonPage):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    # phone = models.CharField(verbose_name=u'Телефон', max_length=256, null=True, blank=True)
    # email = models.EmailField(verbose_name=u'E-mail для приёма заявок', max_length=256, null=True, blank=True)
    coord_x = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Широта')
    coord_y = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Долгота')
    slug = models.SlugField(max_length=100, verbose_name=u'URL', blank=True, null=True)

    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'
        app_label = 'landing'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('landing:city', args=(self.slug,))

    def save(self, *args, **kwargs):
        address = u'город %s' % self.name
        api_key = settings.YANDEX_MAPS_API_KEY
        pos = geocode(api_key, address)
        self.coord_x = float(pos[0])
        self.coord_y = float(pos[1])
        super(City, self).save()


class Video(models.Model):
    title = models.CharField(verbose_name=u'Название', max_length=256)
    code = models.TextField(verbose_name=u'HTML код видео')
    main = models.BooleanField(verbose_name=u'Главное видео', default=False)

    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'
        app_label = 'landing'

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        Video.objects.filter(main=True).update(main=False)
        super(Video, self).save()
