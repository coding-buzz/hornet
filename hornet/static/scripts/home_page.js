var homepage = {
    skillBars: [],
    expandedSkillBarClassName: 'expanded',


    init: function() {
        this.initScrollBarsAnimation();
        this.initImageSlider();
        this.initFeaturedImageScale();
    },

    initScrollBarsAnimation: function() {
        this.skillBars = $('.skill-bar').toArray();

        $(window).scroll(function() {
            this.expandVisibleSkillBars();
            this.removeExpandedSkillBarsFromList();
        }.bind(this));
    },

    initImageSlider: function() {
        $('.companies-carousel .images-wrapper').append(
            $('.companies-carousel .images-wrapper').html()
        );
        $('.companies-carousel').imageslider({
            slideItems: '.image',
            slideContainer: '.images-wrapper',
            slideDuration: 20
        });
    },

    expandVisibleSkillBars: function() {
        $(this.skillBars).each(function(index, skillBar) {
            this.expandSkillBarIfVisible(skillBar);
        }.bind(this));
    },

    expandSkillBarIfVisible: function(skillBar) {
        if (this.isScrolledIntoView(skillBar)) {
            $(skillBar).addClass(this.expandedSkillBarClassName);
        }
    },

    isScrolledIntoView: function(element) {
        var $element = $(element);
        var $window = $(window);
        var docViewTop = $window.scrollTop();
        var docViewBottom = docViewTop + $window.height();
        var elemTop = $element.offset().top;
        var elemBottom = elemTop + $element.height();
        return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
    },

    removeExpandedSkillBarsFromList: function() {
        $(this.skillBars).each(function(index, skillBar) {
            if ($(skillBar).hasClass(this.expandedSkillBarClassName)) {
                this.skillBars.splice(this.skillBars.indexOf(skillBar), 1);
            }
        }.bind(this));
    },

    initFeaturedImageScale: function() {
        this.scaleFeaturedImage();
        $(window).resize(this.scaleFeaturedImage);
    },

    scaleFeaturedImage: function() {
        var imageHeight = $('.featured-image img').height();
        $('.featured-image').height(imageHeight);
    }
}


$(function() {
    homepage.init();
});