# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin, SortableTabularInline, SortableStackedInline

from .models import Setup, City, CityHouse, Video, Why, Service, Review, Thanks, Gallery, Client, Cost, CostImage, \
    CostItem

__author__ = 'alexy'


class MySortableModelAdmin(SortableModelAdmin):
    sortable = 'order'


class MySortableTabularModelAdmin(SortableTabularInline):
    sortable = 'order'


class SetupAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'phone')

    def has_add_permission(self, request):
        if request.user.is_superuser:
            if self.model.objects.count() < 1:
                return True
            else:
                return False
        else:
            return False


class CityHouseAdmin(MySortableTabularModelAdmin):
    model = CityHouse
    # fields = ('city', 'address', 'image')
    # readonly_fields = ('pic', )
    exclude = ['coord_x', 'coord_y']
    suit_classes = 'suit-tab suit-tab-cities'
    extra = 0


class OwnerCityHouseAdmin(MySortableModelAdmin):
    list_display = ('address', 'pic')
    readonly_fields = ('pic', )
    fieldsets = (
        (u'Основные настройки', {
            'fields': ('city', 'address', 'image', 'pic'),
        }),
        (u'Координаты', {
            'classes': ('collapse', ),
            'fields': ('coord_x', 'coord_y'),
        }),
    )

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if not request.user.is_superuser:
            context['adminform'].form.fields['city'].queryset = City.objects.filter(owner=request.user)
            context['adminform'].form.fields['city'].initial = City.objects.filter(owner=request.user).first()
        return super(OwnerCityHouseAdmin, self).render_change_form(request, context)

    def get_queryset(self, request):
        if request.user.is_superuser:
            qs = CityHouse.objects.none()
        else:
            qs = CityHouse.objects.filter(city__owner=request.user)
        return qs


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'coord_x', 'coord_y', 'pic')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('pic', )
    inlines = (CityHouseAdmin, )
    fieldsets = (
        (u'Основные настройки', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('name', 'owner', 'logo', 'pic'),
        }),
        (u'Информация для сайта', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('phone', 'email', 'contact'),
        }),
        (u'Координаты', {
            'classes': ('collapse', 'suit-tab', 'suit-tab-general'),
            'fields': ('coord_x', 'coord_y'),
        }),
        (u'SEO', {
            'classes': ('suit-tab', 'suit-tab-seo'),
            'fields': ('meta_title', 'meta_desc', 'meta_key', 'slug'),
        }),
    )
    suit_form_tabs = (('general', u'Информация по городу'), ('seo', u'СЕО'), ('cities', u'Адреса'))


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
admin.site.register(CityHouse, OwnerCityHouseAdmin)
