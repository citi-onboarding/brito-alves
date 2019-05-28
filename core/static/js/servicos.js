$('#modal-btn').click(function() {
    $('#modal-wrapper').css("display", "block");

    $('#modal-slick').slick({
        nextArrow: `
    <button class="slick-next" type="button" style="display: block;">
        <img class="slick-arrow" alt="right arrow" src="${static}/icons/right-arrow.svg">
    </button>
`,
        prevArrow: `
    <button class="slick-prev" type="button" style="display: block;">
        <img class="slick-arrow" alt="left arrow" src="${static}/icons/left-arrow.svg">
    </button>
`,
    });

});

$('#close-btn').click(function() {
    $('#modal-wrapper').css("display", "none");
});