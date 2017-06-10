ymaps.ready(function () {
  var myMap;
  var current_url = window.location.href;
  var mapBlock = $('#photoMap');
  var url = mapBlock.data('url');
  var city, city_id;
  city = mapBlock.data('city');
  city_id = mapBlock.data('city-id');
  var zoom = 4;
  if (city_id){
    zoom = 10
  }
  var coord = '';
  var myGeocoder = ymaps.geocode(city);
  myGeocoder.then(
    function (res) {
      coord = res.geoObjects.get(0).geometry.getCoordinates();
      myMap = new ymaps.Map("photoMap", {
        center: coord,
        zoom: zoom
      });
      $.ajax({
        type: "POST",
        url: url,
        data: {
          city_id: city_id
        }
      }).done(function (data) {
        var item_list, i, len;
        if (data.house_list.length) {
          item_list = data.house_list;
          for(i = 0, len = item_list.length; i < len; i++) {
            myMap.geoObjects.add(
              new ymaps.Placemark([item_list[i]['coord_y'], item_list[i]['coord_x']], {
              balloonContent: item_list[i]['address'],
              balloonContentBody: '<a href="' + current_url +'#gallery" class="fancybox">Галерея</a><br/><img src="' + item_list[i]['image'] +'" style="width:150px"/><br/><strong>' + item_list[i]['address'] +'</strong>',
              hintContent: item_list[i]['address']
              })
            );
          }
        } else {
          item_list = data.city_list;
          for(i = 0, len = item_list.length; i < len; i++) {
            myMap.geoObjects.add(
              new ymaps.Placemark([item_list[i]['coord_y'], item_list[i]['coord_x']], {
              balloonContent: item_list[i]['name'],
              balloonContentBody: '<a href="' + item_list[i]['city_url'] +'" class="fancybox">Перейти к городу</a><br/><strong>' + item_list[i]['name'] + '(адресов: '+ item_list[i]['count'] +')</strong>',
              hintContent: item_list[i]['name']
              })
            );
          }
        }
      });
    }
  );
});