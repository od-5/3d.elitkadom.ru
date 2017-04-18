# coding=utf-8
from django.db import models

__author__ = 'alexey'


class Common(models.Model):
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created', ]


class CommonPage(Common):
    contact = models.TextField(verbose_name=u'Наши контакты', blank=True, null=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=256, null=True, blank=True)
    email = models.EmailField(verbose_name=u'E-mail для приёма заявок', max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META заголовок')
    meta_key = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META ключевые слова')
    meta_desc = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META описание')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.meta_title


class SortableModel(models.Model):
    order = models.PositiveIntegerField(verbose_name=u'Сортировка', default=1)

    class Meta:
        abstract = True
