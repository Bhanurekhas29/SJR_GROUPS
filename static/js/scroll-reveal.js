document.addEventListener('DOMContentLoaded', function () {
    var selectors = [
        '.about__stat',
        '.vm__card',
        '.business-item',
        '.standard__item',
        '.video-featured',
        '.video-list__item',
        '.gallery__item',
        '.social-card',
        '.faq-item',
        '.contact__card',
        '.cta-banner__inner',
    ];

    var elements = document.querySelectorAll(selectors.join(','));
    if (!elements.length) return;

    if (!('IntersectionObserver' in window)) {
        elements.forEach(function (el) { el.classList.add('is-visible'); });
        return;
    }

    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    elements.forEach(function (el) {
        el.classList.add('reveal');
        observer.observe(el);
    });
});
