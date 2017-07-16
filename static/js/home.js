let locationPreferenceKey = "kathmandu-kitchen-location-preference";
let languagePreferenceKey = "kathmandu-kitchen-language-preference";

$(document).ready(function() {
    $('#our-menu .menu-item').on('click', function() {
        let prev = $('#our-menu .menu-item.expanded');

        prev.find('img').slideUp();
        prev.find('.description').slideUp();
        prev.removeClass('expanded');

        if(!$(this).is(prev)) {
            $(this).find('img').slideDown();
            $(this).find('.description').slideDown();
            $(this).addClass('expanded');
        }

    });
    $('.selected-category-wrapper').on('click', function(){
        if ($('.category-list').is(':visible')){
            $('.selected-category-wrapper').removeClass('open');
            $('.category-list').slideUp();
        }
        else {
            $('.selected-category-wrapper').addClass('open');
            $('.category-list').slideDown();
        }
    });
    $('.hamburger-item').on('click', function(){
        showModal('#hamburger-modal', $(this));
    });

    $('#our-menu .expand-menu-group-btn').on('click', function() {
        //$(this).closest('.menu-group').toggleClass('expanded').find('.content').slideToggle();
        showModal('#our-menu-modal', $(this).closest('.menu-group'));
    });

    $('.btn-close-modal').on('click', function() {
        $(this).closest('.modal').fadeOut(function() {
            $('#modal-container').hide();
            $('html').css('overflow', 'auto');
        });
    });

    $('#our-menu-modal .category-list a').on('click', function() {
        showMenuItem(this);
    });

    if (typeof(Storage) !== "undefined") {
        let languagePreference = localStorage.getItem(languagePreferenceKey);
        let locationPreference = localStorage.getItem(locationPreferenceKey);

        if (!locationPreference) {
            locationPreference = localStorage.setItem(locationPreferenceKey, currentBranchCode);
            //showConfigModal();
        } else {
            /*
            setTimeout( () => {
                $(`#location-select-wrap button[data-branch-code="${locationPreference}"]`).trigger('click');
            }, 0);
            */
        }
    } else {
        // No Web Storage support :/
    }


    $('#navigate-down-btn').on('click', function() {
        $('html, body').animate({
            scrollTop: $('#our-menu').offset().top
        }, 500);
    });

    $('#menu-contact-us, #ham-menu-contact-us').on('click', function() {
        $('html, body').animate({
            scrollTop: $('#contact-us').offset().top
        }, 500);
        $('.btn-close-modal').trigger('click');
    });

    $('#menu-opening-hours, #ham-menu-opening-hours').on('click', function() {
        $('html, body').animate({
            scrollTop: $('#opening-hours').offset().top
        }, 500);
        $('.btn-close-modal').trigger('click');
    });

    $('#menu-see-menu, #ham-menu-see-menu').on('click', function() {
        $('html, body').animate({
            scrollTop: $('#our-menu').offset().top
        }, 500);
        $('.btn-close-modal').trigger('click');
    });

    $('#menu-make-reservations, #ham-menu-reserve').on('click', function() {
        $('html, body').animate({
            scrollTop: $('#reservation-section').offset().top
        }, 500);
        $('.btn-close-modal').trigger('click');
    });

    if (localStorage.getItem('noredirect')) {
        localStorage.removeItem('noredirect');
        $('.ghost').removeClass('ghost');
        $('#location-select-wrap').addClass('ghost');
        $('html').css('overflow', 'auto');
    }
     
    $('#location-select-wrap button').on('click', function() {
        localStorage.setItem(locationPreferenceKey, $(this).data('branch-code'));
        if($(this).data('branch-code') == currentBranchCode) {
            localStorage.removeItem('noredirect');
            $('.ghost').removeClass('ghost');
            $('#location-select-wrap').addClass('ghost');
            $('html').css('overflow', 'auto');
        } else {
            localStorage.setItem('noredirect', true);
            window.location.href = $(this).data('href');
        }
    });

    $('html').css('overflow', 'auto');
});


function clearConfigSession() {
    localStorage.removeItem(languagePreferenceKey);
    localStorage.removeItem(locationPreferenceKey);
}


function showConfigModal() {
    $('#modal-container').show();
    $('#config-modal').show();
}

function hideConfigModal() {
    $('#config-modal').hide();
    $('#modal-container').hide();
}

function showModal(modalSelector, clickInvokerSelector) {
    $('html').css('overflow', 'hidden');
    let invoker = $(clickInvokerSelector);
    let pos = invoker.offset();
    let width = invoker.outerWidth();
    let height = invoker.outerHeight();

    $(modalSelector).find('.content').hide();

    $(modalSelector).css({
        'left': pos.left,
        'top': pos.top - $(window).scrollTop(),
        'width': width,
        'height': height,
        'opacity': '0.5',
    });

    $('#modal-container').show();
    $(modalSelector).show();
    $(modalSelector).animate({
        'opacity': '1',
        'left': '0',
        'top': '0',
        'width': '100%',
        'height': '100%',
    }, 300, function() {
        $(modalSelector).find('.content').fadeIn();
    });

    showMenuItem($('a[data-target="'+$(clickInvokerSelector).data('target')+'"]'));
}

function showMenuItem(callerElementSelector) {
    let caller = $(callerElementSelector);
    caller.addClass('active');
    caller.siblings().removeClass('active');

    let callerText = caller.text();
    $('#category-name').text(callerText);

    if ($('.selected-category-wrapper').is(':visible')){
        $('.category-list').slideUp();
        $('.selected-category-wrapper').removeClass('open');
    }

    let target = $($(callerElementSelector).data('target'));
    target.siblings().removeClass('active');
    target.siblings().hide();

    target.addClass('active');
    target.show();
}
