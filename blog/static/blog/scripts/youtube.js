$(function() {
    var iframeRatio = 0.5625;

    function resizeYoutubeFrames() {
        $('.yt-frame').each(function() {
            var height = $(this).width() * iframeRatio;
            $(this).css('height', height + 'px');
        });
    }

    resizeYoutubeFrames();
    $(window).resize(resizeYoutubeFrames);
});