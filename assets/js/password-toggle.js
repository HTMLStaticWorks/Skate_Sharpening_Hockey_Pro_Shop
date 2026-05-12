document.addEventListener('DOMContentLoaded', () => {
    const toggleButtons = document.querySelectorAll('.password-toggle-btn');

    toggleButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const wrapper = btn.closest('.password-field-wrapper');
            const input = wrapper.querySelector('input');
            const icon = btn.querySelector('i');

            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.remove('bi-eye');
                icon.classList.add('bi-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.remove('bi-eye-slash');
                icon.classList.add('bi-eye');
            }
        });
    });
});
