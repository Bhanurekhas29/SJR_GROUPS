document.addEventListener('DOMContentLoaded', function () {
    var items = document.querySelectorAll('.faq-item');
    if (!items.length) return;

    items.forEach(function (item) {
        var question = item.querySelector('.faq-item__question');
        question.addEventListener('click', function () {
            var wasOpen = item.classList.contains('is-open');
            items.forEach(function (i) { i.classList.remove('is-open'); });
            if (!wasOpen) {
                item.classList.add('is-open');
            }
        });
    });
});
