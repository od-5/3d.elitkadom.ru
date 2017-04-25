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
        if (data.house_list.length) {
          var item_list = data.house_list;
          for(var i = 0, len = item_list.length; i < len; i++) {
            myMap.geoObjects.add(
              new ymaps.Placemark([item_list[i]['coord_y'], item_list[i]['coord_x']], {
              balloonContent: item_list[i]['address'],
              balloonContentBody: '<a href="' + current_url +'#gallery" class="fancybox">Галлерея</a><br/><img src="' + item_list[i]['image'] +'" style="width:150px"/><br/><strong>' + item_list[i]['address'] +'</strong>',
              hintContent: item_list[i]['address']
              })
            );
          }
        } else {
          var item_list = data.city_list;
          for(var i = 0, len = item_list.length; i < len; i++) {
            myMap.geoObjects.add(
              new ymaps.Placemark([item_list[i]['coord_y'], item_list[i]['coord_x']], {
              balloonContent: item_list[i]['name'],
              balloonContentBody: '<a href="' + current_url +'#gallery" class="fancybox">Галлерея</a><br/><strong>' + item_list[i]['name'] + '(адресов: '+ item_list[i]['count'] +')</strong>',
              hintContent: item_list[i]['name']
              })
            );
          }
        }
      });
    }
  );





  //var photo_list = '';
  //var map_block = $('#photoMap');
  //var url = map_block.data('url');
  ////var city = $('#id_a_city').val();
  //$.ajax({
  //  type: "POST",
  //  async: false,
  //  url: url
  //  //data: {
  //  //  city: city,
  //  //}
  //}).done(function (data) {
  //  console.log(data);
  //  console.log(data.length);
  //
  //});
  //if (photo_list.length){
  //  center = [photo_list[0]['coord_y'], photo_list[0]['coord_x']];
  //} else {
  //  center = [48.713339, 44.497116]
  //}
  //var myMap = new ymaps.Map('photoMap', {
  //  center: center,
  //  zoom: 4,
  //  behaviors: ['default', 'scrollZoom']
  //}, {
  //  searchControlProvider: 'yandex#search'
  //}),
  //  clusterer = new ymaps.Clusterer({
  //  preset: 'islands#invertedVioletClusterIcons',
  //  groupByCoordinates: false,
  //  clusterDisableClickZoom: true,
  //  clusterHideIconOnBalloonOpen: false,
  //  geoObjectHideIconOnBalloonOpen: false
  //}),
  //  getPointData = function (index) {
  //  return {
  //    balloonContentBody: '<img src="' + photo_list[index]['image'] +'" style="width:150px"/><br/><strong>' + photo_list[index]['surface'] + ', ' + photo_list[index]['porch'] + '</strong>',
  //    clusterCaption: '<span>' + photo_list[index]['surface'] + '</span>'
  //  };
  //},
  //  getPointOptions = function () {
  //  return {
  //    preset: 'islands#violetIcon'
  //  };
  //},
  ////points = photo_points,
  //geoObjects = [];
  //for(var i = 0, len = photo_list.length; i < len; i++) {
  //  geoObjects[i] = new ymaps.Placemark([photo_list[i]['coord_y'], photo_list[i]['coord_x']], getPointData(i), getPointOptions());
  //}
  //clusterer.options.set({
  //  gridSize: 80,
  //  clusterDisableClickZoom: true
  //});
  //
  //clusterer.add(geoObjects);
  //myMap.geoObjects.add(clusterer);


  //myMap.setBounds(clusterer.getBounds(), {
  //    checkZoomRange: true
  //});
});