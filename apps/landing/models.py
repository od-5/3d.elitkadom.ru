# coding=utf-8
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

from core.base_model import CommonPage, SortableModel
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


class CityHouse(SortableModel):
    city = models.ForeignKey(to=City, verbose_name=u'Город')
    address = models.CharField(verbose_name=u'Адрес', max_length=256)
    coord_x = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Широта')
    coord_y = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Долгота')
    image = models.ImageField(verbose_name=u'Обложка', upload_to='cityhouse/')
    image_resize = ImageSpecField(
        [SmartResize(*settings.HOUSE_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    class Meta:
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреса'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.address

    def pic(self):
        return '<img src="%s" width="120"/>' % self.image_resize.url

    pic.short_description = u"Миниатюра"
    pic.allow_tags = True

    def save(self, *args, **kwargs):
        address = u'город %s %s' % (self.city.name, self.address)
        api_key = settings.YANDEX_MAPS_API_KEY
        pos = geocode(api_key, address)
        self.coord_x = float(pos[0])
        self.coord_y = float(pos[1])
        super(CityHouse, self).save()


class Video(SortableModel):
    title = models.CharField(verbose_name=u'Название', max_length=256)
    code = models.TextField(verbose_name=u'HTML код видео')
    main = models.BooleanField(verbose_name=u'Главное видео', default=False)

    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.main:
            Video.objects.filter(main=True).update(main=False)
            self.main = True
        super(Video, self).save()


class Why(SortableModel):
    text = models.TextField(verbose_name=u'Текст')

    class Meta:
        verbose_name = u'Почему заказывают рекламу у нас'
        verbose_name_plural = u'Поччему заказывают рекламу у нас'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.text


class Service(SortableModel):
    title = models.CharField(verbose_name=u'Название', max_length=256)
    text = models.TextField(verbose_name=u'Текст')
    price = models.CharField(verbose_name=u'Стоимость', max_length=500)
    cover = models.ImageField(verbose_name=u'Обложка', upload_to='service/')

    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'Наши услуги'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.title

    def pic(self):
        return '<img src="%s" width="170"/>' % self.cover.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True


class Review(SortableModel):
    name = models.CharField(verbose_name=u'ФИО', max_length=256)
    desc = models.CharField(verbose_name=u'подпись', max_length=256)
    text = models.TextField(verbose_name=u'Текст')
    avatar = models.ImageField(verbose_name=u'Обложка', upload_to='review/')

    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s" width="170"/>' % self.avatar.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True


class Thanks(SortableModel):
    name = models.CharField(verbose_name=u'Название или ФИО', max_length=256)
    desc = models.CharField(verbose_name=u'Подпись', max_length=256, blank=True, null=True)
    image = models.ImageField(verbose_name=u'Благодарственно письмо', upload_to='thanks/')
    image_resize = ImageSpecField(
        [SmartResize(*settings.THANKS_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    class Meta:
        verbose_name = u'Благодарственное письмо'
        verbose_name_plural = u'Благодарственные письма'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s" width="120"/>' % self.image_resize.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True


class Gallery(SortableModel):
    image = models.ImageField(verbose_name=u'Изображение', upload_to='gallery/')
    image_resize = ImageSpecField(
        [SmartResize(*settings.GALLERY_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    class Meta:
        verbose_name = u'Галлерея'
        verbose_name_plural = u'Галлерея'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return u'Изображение #%s' % self.id

    def pic(self):
        return '<img src="%s" width="120"/>' % self.image_resize.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True


class Client(SortableModel):
    image = models.ImageField(verbose_name=u'Логотип', upload_to='client/')
    maket = models.ImageField(verbose_name=u'макет', upload_to='client/', blank=True, null=True)

    class Meta:
        verbose_name = u'Клиент'
        verbose_name_plural = u'Клиенты'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return u'Изображение #%s' % self.id

    def get_maket_url(self):
        if self.maket:
            return self.maket.url
        else:
            return self.image.url

    def pic(self):
        return '<img src="%s" width="120"/>' % self.image.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True


class Cost(SortableModel):
    title = models.CharField(verbose_name=u'Наименование', max_length=256)

    class Meta:
        verbose_name = u'Стоимость'
        verbose_name_plural = u'Стоимость'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.title


class CostItem(SortableModel):
    cost = models.ForeignKey(to=Cost, verbose_name=u'Стоимость')
    title = models.CharField(verbose_name=u'Наименование', max_length=256)
    price = models.CharField(verbose_name=u'Стоимость', max_length=256)

    class Meta:
        verbose_name = u'Пункт'
        verbose_name_plural = u'Пукнты'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return self.title


class CostImage(SortableModel):
    cost = models.ForeignKey(to=Cost, verbose_name=u'Стоимость')
    image = models.ImageField(verbose_name=u'Изображение', upload_to='cost/')
    image_resize = ImageSpecField(
        [SmartResize(*settings.COST_IMAGE_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    class Meta:
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'
        app_label = 'landing'
        ordering = ('order', )

    def __unicode__(self):
        return u'Изображение #%s' % self.id

    def pic(self):
        if self.image:
            return '<img src="%s" width="120"/>' % self.image_resize.url
        else:
            return '----'
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True
