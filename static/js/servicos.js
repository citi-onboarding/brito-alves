$('#modal-btn').click(function() {
    $('#modal-wrapper').fadeIn(300);

    $('#modal-slick').slick({
        nextArrow: `
    <button class="slick-next" type="button" style="display: block;">
        <img class="slick-arrow" alt="right arrow" src="${static}/icons/arrow-right-modal.svg">
    </button>
`,
        prevArrow: `
    <button class="slick-prev" type="button" style="display: block;">
        <img class="slick-arrow" alt="left arrow" src="${static}/icons/arrow-left-modal.svg">
    </button>
`,
    });

});

$('#close-btn').click(function() {
    //$('#modal-wrapper').hide();

    $('#modal-wrapper').css("display", "none");

    $('#modal-slick').slick('unslick');
});