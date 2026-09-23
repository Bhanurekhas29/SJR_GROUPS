document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.querySelector('.site-header__toggle');
    var nav = document.querySelector('.site-header__nav');
    if (!toggle || !nav) return;

    toggle.addEventListener('click', function () {
        nav.classList.toggle('is-open');
    });
});
