document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('enquiry-form');
    if (!form) return;

    var status = form.querySelector('.contact__form-status');

    if (form.phone) {
        form.phone.addEventListener('input', function () {
            form.phone.value = form.phone.value.replace(/\D/g, '');
        });
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        var data = {
            name: form.name.value,
            phone: form.phone.value,
            email: form.email.value,
            business: form.business.value,
            message: form.message.value,
        };

        status.textContent = 'Sending...';
        status.className = 'contact__form-status';

        fetch('/api/contact/submit/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        })
            .then(function (res) { return res.json().then(function (body) { return { ok: res.ok, body: body }; }); })
            .then(function (result) {
                if (result.ok) {
                    status.textContent = 'Thanks! We\'ll be in touch soon.';
                    status.className = 'contact__form-status is-success';
                    form.reset();
                } else {
                    status.textContent = result.body.error || 'Something went wrong. Please try again.';
                    status.className = 'contact__form-status is-error';
                }
            })
            .catch(function () {
                status.textContent = 'Something went wrong. Please try again.';
                status.className = 'contact__form-status is-error';
            });
    });
});
