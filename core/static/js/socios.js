$(document).ready(function () {
  $('.socios-row').slick({
    dots: true,
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1050,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
        }
      }, {
        breakpoint: 900,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          centerMode: true,
        }
      },
    ],
    nextArrow: `
    <button class="arrow-btn arrow-right" type="button">
        <img src="../static/assets/icons/arrow-right.svg" alt="Seta para o próximo slide do carrossel">
    </button>
    `,
    prevArrow: `
    <button class="arrow-btn arrow-left" type="button">
        <img src="../static/assets/icons/arrow-left.svg" alt="Seta para o próximo slide do carrossel">
    </button>
    `,
  });
});