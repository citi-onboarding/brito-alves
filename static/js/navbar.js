let opened = false;

const fechar = () => {
    const navbarMobile = document.querySelector('#nav .navbar-mobile');
    navbarMobile.style.display = 'none';
    opened = false;
}

const abrir = () => {
    const navbarMobile = document.querySelector('#nav .navbar-mobile');
    navbarMobile.style.display = 'flex';
    opened = true;
}

const menuClick = () => {
    if (opened) {
        fechar();
    } else {
        abrir();
    }
};

window.onresize = () => {
    const x = window.matchMedia('(max-width: 770px)');
    if (!x.matches) {
        fechar();
    }
};