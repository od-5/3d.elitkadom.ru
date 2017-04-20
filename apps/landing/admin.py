# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin, SortableTabularInline

from .models import Setup, City, Video, Why, Service, Review, Thanks, Gallery, Client, Cost, CostImage, CostItem

__author__ = 'alexy'


class SetupAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'phone')

    def has_add_permission(self, request):
        if self.model.objects.count() < 1:
            return True
        else:
            return False


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'coord_x', 'coord_y')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (u'Основные настройки', {
            'fields': ('name',),
        }),
        (u'Информация для сайта', {
            'fields': ('phone', 'email', 'contact'),
        }),
        (u'Координаты', {
            'fields': ('coord_x', 'coord_y'),
            'classes': ('collapse',),
        }),
        (u'SEO', {
            'fields': ('meta_title', 'meta_desc', 'meta_key', 'slug'),
            'classes': ('collapse',),
        }),
    )


class MySortableModelAdmin(SortableModelAdmin):
    sortable = 'order'


class MySortableTabularModelAdmin(SortableTabularInline):
    sortable = 'order'


class VideoAdmin(MySortableModelAdmin):
    list_display = ('title', 'main')


class WhyAdmin(MySortableModelAdmin):
    list_display = ('text', )


class ServiceAdmin(MySortableModelAdmin):
    list_display = ('title', 'price', 'pic')


class ReviewAdmin(MySortableModelAdmin):
    list_display = ('name', 'desc', 'pic')


class ThanksAdmin(MySortableModelAdmin):
    list_display = ('name', 'desc', 'pic')


class GalleryAdmin(MySortableModelAdmin):
    list_display = ('__unicode__', 'pic')


class ClientAdmin(MySortableModelAdmin):
    list_display = ('__unicode__', 'pic')


class CostItemAdmin(MySortableTabularModelAdmin):
    model = CostItem
    list_display = ('cost', 'title', 'price')
    extra = 0


class CostImageAdmin(MySortableTabularModelAdmin):
    model = CostImage
    fields = ('cost', 'image', 'pic')
    readonly_fields = ('pic', )
    extra = 0


class CostAdmin(MySortableModelAdmin):
    list_display = ('title', )
    inlines = (CostItemAdmin, CostImageAdmin)

admin.site.register(Setup, SetupAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Why, WhyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Thanks, ThanksAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Cost, CostAdmin)
