# coding=utf-8
from annoying.decorators import ajax_request

from django.views.decorators.csrf import csrf_exempt

from .models import City, CityHouse

__author__ = 'alexy'


@csrf_exempt
@ajax_request
def city_map(request):
    city_id = request.POST.get('city_id') or None
    city_list = []
    house_list = []
    if city_id:
        for i in CityHouse.objects.filter(city=int(city_id)):
            house_list.append({
                'address': i.address,
                'coord_x': float(i.coord_x),
                'coord_y': float(i.coord_y),
                'image': i.image.url
            })
    else:
        for i in City.objects.all():
            city_list.append({
                'name': i.name,
                'coord_x': float(i.coord_x),
                'coord_y': float(i.coord_y),
                'count': i.cityhouse_set.count(),
                'city_url': i.get_absolute_url()
            })
    return {
        'house_list': house_list,
        'city_list': city_list
    }
