$(function() {
    var skillBars = $('.skill-bar').toArray();

    $(window).scroll(function() {
        $(skillBars).each(function() {
            if (isScrolledIntoView(this)) {
                skillBars.splice(skillBars.indexOf(this), 1);
                $(this).addClass('expanded');
            }
        });
    });

    function isScrolledIntoView(elem) {
        var $elem = $(elem);
        var $window = $(window);

        var docViewTop = $window.scrollTop();
        var docViewBottom = docViewTop + $window.height();

        var elemTop = $elem.offset().top;
        var elemBottom = elemTop + $elem.height();

        return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
    }
});