
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
    $('.navbar').addClass('scroll_effect');
}
else{
    $('.navbar').removeClass('scroll_effect');
}
