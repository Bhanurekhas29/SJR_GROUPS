document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('video-modal');
    if (!modal) return;

    var player = modal.querySelector('.video-modal__player');
    var closeBtn = modal.querySelector('.video-modal__close');
    var backdrop = modal.querySelector('.video-modal__backdrop');

    function openModal(src) {
        player.src = src;
        modal.classList.add('is-open');
        player.play();
    }

    function closeModal() {
        modal.classList.remove('is-open');
        player.pause();
        player.removeAttribute('src');
        player.load();
    }

    document.querySelectorAll('[data-video-src]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            openModal(link.dataset.videoSrc);
        });
    });

    closeBtn.addEventListener('click', closeModal);
    backdrop.addEventListener('click', closeModal);
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
    });
});
