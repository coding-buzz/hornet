var homepage = {
    skillBars: [],
    expandedSkillBarClassName: 'expanded',


    init: function() {
        this.initScrollBarsAnimation();
        this.initSkillsLegend();
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

    initSkillsLegend: function() {
        $('.skills-legend .breakpoint').on('mouseenter', function() {
            $(this).addClass('active');
            var breakpointLevel = parseInt($(this).data('level'));
            var from = 0;
            var to = 50;
            if (breakpointLevel == 2) {
                from = 51;
                to = 100;
            }
            $('.skills-legend .breakpoint:not(.active)').addClass('hidden');
            $('.skills .skill').each(function() {
                var skillLevel = parseInt($(this).data('level'));
                if (skillLevel < from || skillLevel > to) {
                    $(this).addClass('hidden');
                }
            });
        });

        $('.skills-legend .breakpoint').on('mouseleave', function() {
            $('.skills-legend .breakpoint').removeClass('active').removeClass('hidden');
            $('.skills .skill').removeClass('hidden');
        });
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
        if (imageHeight == 0) {
            setTimeout(function() {
                this.scaleFeaturedImage();
            }.bind(this), 100);
        }
    }
}


$(function() {
    homepage.init();
});