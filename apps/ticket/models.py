# coding=utf-8
from django.db import models

from apps.landing.models import City
from core.base_model import Common

__author__ = 'alexy'


class Ticket(Common):
    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'ticket'

    def __unicode__(self):
        return self.name

    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Выполнено'),
        (3, u'Отмена'),
    )

    city = models.ForeignKey(to=City, verbose_name=u'Город', blank=True, null=True)
    house = models.CharField(verbose_name=u'Дома или ЖК', max_length=256)
    phone = models.CharField(verbose_name=u'Телефон или email', max_length=256)
    status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки',  choices=TICKET_STATUS_CHOICE,
                                              default=0, blank=True, null=True)
    theme = models.CharField(verbose_name=u'Тема', max_length=256)
