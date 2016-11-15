$(function() {
    var menubar = $('.menubar');
    var options = menubar.find('.options');
    var expander = menubar.find('.expander.clickable');

    expander.on('click', function() {;
        menubar.toggleClass('expanded');
        options.slideToggle();
    });
});