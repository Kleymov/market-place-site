$('#showCategory').click(function(){
    $('.categories').css('display', 'flex');
    $('.swiper-button-prev').css('top', '60%');
    $('.swiper-button-next').css('top', '60%');
});
$('#exitFromCategory').click(function(){
    $('.categories').css('display', 'none');
    $('.swiper-button-prev').css('top', '35%');
    $('.swiper-button-next').css('top', '35%');
});