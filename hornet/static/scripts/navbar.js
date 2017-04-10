$(function() {
    var nav = $('nav');
    var scrollDistanceThreshold = 110;

    $(document).scroll(function() {
        var scrollDistance = $(this).scrollTop();
        nav.toggleClass('mini', scrollDistance >= scrollDistanceThreshold);
    });


    $('.home-link').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0 }, 'slow');
        return false;
    });
});