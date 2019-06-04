window.onscroll = function() {stickyFunction()};

const navbarWeb = document.querySelector('#nav .navbar-web');
const navbarLogoWeb = document.querySelector('.navbar-logo-web');
const logoImg = document.querySelector('.logo-only');
const logoText = document.querySelector('.logo-name');
console.log(navbarLogoWeb.offsetLeft);
console.log(logoImg.offsetLeft);
const offset = logoImg.offsetLeft - navbarLogoWeb.offsetLeft - 3;

const stickyFunction = () => {
  if (window.pageYOffset >= 100) {
    navbarWeb.style.height = '8vh';
    logoText.style.display = 'none';
    logoImg.style.marginLeft = `${offset}px`;
    logoImg.style.height = '7vh';
  } else {
    navbarWeb.style.height = '12vh';
    logoText.style.display = 'initial';
    logoImg.style.margin = '0 auto';
    logoImg.style.height = '6vh';
  }
};

stickyFunction();