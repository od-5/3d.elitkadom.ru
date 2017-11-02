$(document).ready(function () {

  // fancybox
  jQuery('.fancybox').fancybox();
  // popup close
  $(document).on('click','.popup-close',function(e){
    e.preventDefault();
    $.fancybox.close();
  });

  $(".input[name='phone']").mask("+7 (999) 999-99-99");
  $('form').each(function(){
    $(this).validate({
      rules: {
        phone: {
          required: true,
          minlength: 3
        },
        name: {
          required: true,
          minlength: 3
        }
      }
    });
  });

  // scroll
  $(window).scroll( function(){
    if ($(this).scrollTop() > 100){
      $('.header-fixed').addClass('fixed');
    }else{
      $('.header-fixed').removeClass('fixed');
    }

  });
  //$('.scroll').click(function(e){
  //  e.preventDefault();
  //  var selected = $(this).attr('href').replace('/', '');
  //  $.scrollTo(selected, 1000, {offset: 50});
  //  return false;
  //});

  // video button
  $(document).on('click','.header-play',function(e){
    e.preventDefault();
    $('.tablet-hidden').show();
  });
  // button info
  $(document).on('click','.button-data',function(e){
    e.preventDefault();
    var data_title = $(this).attr('data-title');
    var data_button = $(this).attr('data-button');
    $('#popup input[name=theme]').val(data_title);
    $('#popup .popup-form-title').text(data_title);
    $('#popup .submit').text(data_button);
  });

  // slider
  $(".product-slider").slick({
    autoplay: false,
    dots: true,
    customPaging : function(slider, i) {
      var thumb = $(slider.$slides[i]).data('thumb');
      return '<a><img src="'+thumb+'"></a>';
    }
  });
  $('.review-slider').slick({
    dots: false,
    speed: 500,
    slidesToShow: 2,
    responsive: [{
      breakpoint: 767,
      settings: {
        slidesToShow: 1,
        dots: false
      }
    }]
  });
  $('.cert-slider').slick({
    dots: false,
    speed: 500,
    slidesToShow: 4,
    responsive: [{
      breakpoint: 960,
      settings: {
        slidesToShow: 3
      }
    },{
      breakpoint: 640,
      settings: {
        slidesToShow: 2
      }
    },{
      breakpoint: 480,
      settings: {
        slidesToShow: 1
      }
    }]
  });


});

