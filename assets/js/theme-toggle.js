document.addEventListener('DOMContentLoaded', () => {
    const themeButtons = document.querySelectorAll('#theme-toggle');
    const body = document.body;

    // Check for saved theme
    const savedTheme = localStorage.getItem('theme') || 'dark-mode';
    applyTheme(savedTheme);

    themeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const currentTheme = body.classList.contains('dark-mode') ? 'dark-mode' : 'light-mode';
            const newTheme = currentTheme === 'dark-mode' ? 'light-mode' : 'dark-mode';
            applyTheme(newTheme);
            localStorage.setItem('theme', newTheme);
        });
    });

    function applyTheme(theme) {
        body.classList.remove('dark-mode', 'light-mode');
        body.classList.add(theme);
        
        themeButtons.forEach(btn => {
            const icon = btn.querySelector('i');
            if (icon) {
                if (theme === 'dark-mode') {
                    icon.classList.remove('bi-moon-fill');
                    icon.classList.add('bi-sun-fill');
                } else {
                    icon.classList.remove('bi-sun-fill');
                    icon.classList.add('bi-moon-fill');
                }
            }
        });
    }
});
