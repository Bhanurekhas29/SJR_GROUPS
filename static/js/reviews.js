document.addEventListener('DOMContentLoaded', function () {
    var slides = document.querySelectorAll('.review-slide');
    var arrows = document.querySelectorAll('.reviews__arrow');
    if (slides.length < 2 || !arrows.length) return;

    var current = 0;

    function show(index) {
        slides[current].classList.remove('is-active');
        current = (index + slides.length) % slides.length;
        slides[current].classList.add('is-active');
    }

    arrows.forEach(function (btn) {
        btn.addEventListener('click', function () {
            show(btn.dataset.dir === 'next' ? current + 1 : current - 1);
        });
    });
});
