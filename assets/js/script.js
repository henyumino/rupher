
$(document).scroll(function() {
    if ($(document).scrollTop() >= 200) {
        $('.scroll_effect').css({
            'height':'56px',
            'boxShadow': '0 10px 20px -4px rgba(0,0,0,.03)',
        })
        $('.navbar-s').removeClass('nav-single');
    } else {
        $('.scroll_effect').css({
            'height':'120px',
            'boxShadow': '',
        })
        $('.navbar-s').addClass('nav-single');
    }
});

    
if($(window).width() !== 360){
    $('.navbar-w').addClass('scroll_effect');
}
else{
    $('.navbar-w').removeClass('scroll_effect');
}


$(function () {
    $('[data-toggle="popover"]').popover()
})

$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

$('.scroll-post').on('click',function(){
    // $("html, body").animate({ scrollTop: 550 }, 1000);
    var $container = $("html,body");
    var $scrollTo = $('.row-single-post');

    $container.animate({scrollTop: $scrollTo.offset().top - $container.offset().top + $container.scrollTop(), scrollLeft: 0},1000);
})

$('#exampleModal').modal('show')