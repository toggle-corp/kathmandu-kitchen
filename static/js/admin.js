$(document).ready(function() {
    $('aside .content .model').on('click', function() {
        showMenuItem(this);
    });

    showMenuItem($('aside .content .model').eq(0));

});

function showMenuItem(caller) {
    let target = $(caller).data('target');

    $(caller).siblings('.active').removeClass('active');
    $(caller).addClass('active');


    $(target).siblings('.active').removeClass('active').hide();
    $(target).addClass('active');
    $(target).show();
}
