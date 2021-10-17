/*global $,jQuery,alert,console*/ 
$(function(){
    'use strict';
    var win_H = $(window).height() - 30 ,
        header_H = $('.header').innerHeight(),
        nav_H = $('.navbar').innerHeight();


        $('.slider-img, .carousel-item').height(win_H - (header_H + nav_H) );

});

$(function(){
    $('.nav-item').on('click',function() {
        $(this).siblings().removeclass('active');
        $(this).addclass('active');
    })
});