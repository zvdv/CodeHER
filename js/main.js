
// Drawer
const drawer = document.querySelector('.drawer-overview');
const openButton = drawer.nextElementSibling;
const closeButton = drawer.querySelector('sl-button[variant="primary"]');

openButton.addEventListener('click', () => drawer.show());
closeButton.addEventListener('click', () => drawer.hide());

// Popup
const container = document.querySelector('.popup-arrow');
const popup = container.querySelector('sl-popup');
const placement = container.querySelector('[name="placement"]');
const arrowPlacement = container.querySelector('[name="arrow-placement"]');
const arrow = container.querySelector('[name="arrow"]');