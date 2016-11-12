$(function() {
    var nav = $('nav');
    var scrollDistanceThreshold = 110;

    $(document).scroll(function() {
        var scrollDistance = $(this).scrollTop();
        nav.toggleClass('mini', scrollDistance >= scrollDistanceThreshold);
    });
});