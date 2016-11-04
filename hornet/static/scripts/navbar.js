$(function() {
    var nav = $('nav');
    var scrollDistanceThreshold = 100;

    $(document).scroll(function() {
        var scrollDistance = $(this).scrollTop();
        nav.toggleClass('mini', scrollDistance >= scrollDistanceThreshold);
    });
});