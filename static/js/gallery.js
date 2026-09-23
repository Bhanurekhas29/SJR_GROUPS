document.addEventListener('DOMContentLoaded', function () {
    var filters = document.querySelectorAll('.gallery__filter');
    var items = document.querySelectorAll('.gallery__item');
    if (!filters.length || !items.length) return;

    filters.forEach(function (btn) {
        btn.addEventListener('click', function () {
            filters.forEach(function (b) { b.classList.remove('is-active'); });
            btn.classList.add('is-active');

            var filter = btn.dataset.filter;
            items.forEach(function (item) {
                var show = filter === 'all' || item.dataset.category === filter;
                item.classList.toggle('is-hidden', !show);
            });
        });
    });
});
