let opened = false;

const fechar = () => {
    const navbarMobile = document.querySelector('#nav .navbar-mobile');
    const navbarBtn = document.querySelector('#nav .navbar-btn');
    navbarMobile.style.display = 'none';
    navbarBtn.style.position = 'absolute';
    opened = false;
}

const abrir = () => {
    const navbarMobile = document.querySelector('#nav .navbar-mobile');
    const navbarBtn = document.querySelector('#nav .navbar-btn');
    navbarMobile.style.display = 'flex';
    navbarBtn.style.position = 'fixed';
    opened = true;
}

const menuClick = () => {
    if (opened) {
        fechar();
    } else {
        abrir();
    }
};