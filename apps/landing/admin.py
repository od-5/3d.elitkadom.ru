# coding=utf-8
from django.contrib import admin
from .models import Setup, City, Video

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


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'main')


admin.site.register(Setup, SetupAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Video, VideoAdmin)
