document.addEventListener('DOMContentLoaded', () => {
    const rtlToggles = document.querySelectorAll('[id^="rtl-toggle"]');
    const html = document.documentElement;

    // Check for saved RTL state
    const savedRtl = localStorage.getItem('rtl') === 'true';
    if (savedRtl) {
        applyRtl(true);
    }

    rtlToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const isRtl = html.getAttribute('dir') === 'rtl';
            applyRtl(!isRtl);
            localStorage.setItem('rtl', !isRtl);
        });
    });

    function applyRtl(enable) {
        if (enable) {
            html.setAttribute('dir', 'rtl');
            html.classList.add('rtl');
        } else {
            html.removeAttribute('dir');
            html.classList.remove('rtl');
        }
        window.dispatchEvent(new Event('resize'));
    }
});
