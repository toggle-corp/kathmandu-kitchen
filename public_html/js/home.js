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

    $('#our-menu .expand-menu-group-btn').on('click', function() {
        //$(this).closest('.menu-group').toggleClass('expanded').find('.content').slideToggle();
        showModal('#our-menu-modal', $(this).closest('.menu-group'));
    });

    $('#our-menu-modal .btn-close-modal').on('click', function() {
        $(this).closest('.modal').fadeOut(function() {
            $('#modal-container').hide();
        }); 
    });

    $('#our-menu-modal .category-list a').on('click', function() {
        showMenuItem(this);
    });

});

function showModal(modalSelector, clickInvokerSelector) {
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

    let target = $($(callerElementSelector).data('target'));
    target.siblings().removeClass('active');
    target.siblings().hide();

    target.addClass('active');
    target.show();
}
