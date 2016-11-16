$(function() {
    var menubar = $('.menubar');
    var options = menubar.find('.options');
    var expander = menubar.find('.expander.clickable');

    expander.on('click', function() {;
        menubar.toggleClass('expanded');
        options.slideToggle();
    });

    // iOS hover hack
    options.find('.option-name').on('touchend', function(e) {
        var parent = $(this).parents('li');
        if (parent.hasClass('hovered')) {
            parent.removeClass('hovered');
        } else {
            options.find('.hovered').removeClass('hovered');
            $(this).parents('li').toggleClass('hovered');
        }
    });

    options.find('> li').on('mouseenter', function() {
        $(this).addClass('hovered');
    });

     options.find('> li').on('mouseleave', function() {
        $(this).removeClass('hovered');
    });
});