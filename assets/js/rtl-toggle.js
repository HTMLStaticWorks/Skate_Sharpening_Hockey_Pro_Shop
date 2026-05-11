document.addEventListener('DOMContentLoaded', () => {
    const rtlToggle = document.getElementById('rtl-toggle');
    const html = document.documentElement;

    // Check for saved RTL state
    const savedRtl = localStorage.getItem('rtl') === 'true';
    if (savedRtl) {
        html.setAttribute('dir', 'rtl');
        html.classList.add('rtl');
    }

    if (rtlToggle) {
        rtlToggle.addEventListener('click', () => {
            const isRtl = html.getAttribute('dir') === 'rtl';
            if (isRtl) {
                html.removeAttribute('dir');
                html.classList.remove('rtl');
                localStorage.setItem('rtl', 'false');
            } else {
                html.setAttribute('dir', 'rtl');
                html.classList.add('rtl');
                localStorage.setItem('rtl', 'true');
            }
            // Trigger a resize event to refresh any layout-dependent scripts (like GSAP/ScrollTrigger)
            window.dispatchEvent(new Event('resize'));
        });
    }
});
