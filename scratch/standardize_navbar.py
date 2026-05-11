import os

pages = {
    'index.html': 'Home',
    'sharpening.html': 'Sharpening',
    'customization.html': 'Customization',
    'repairs.html': 'Repairs',
    'team-orders.html': 'Team Orders',
    'shop.html': 'Shop',
    'blog.html': 'Blog',
    'contact.html': 'Contact'
}

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

def get_navbar(active_page_name):
    links = []
    for href, name in pages.items():
        active_class = ' active" style="color: var(--accent);' if name == active_page_name else ''
        links.append(f'                <li><a href="{href}" class="nav-link{active_class}">{name}</a></li>')
    
    links_html = '\n'.join(links)
    
    return f'''    <!-- Navbar -->
    <nav class="navbar">
        <div class="container">
            <a href="index.html" class="nav-logo">
                <i class="bi bi-lightning-charge-fill accent-glow"></i>
                ICEPRO
            </a>
            
            <ul class="nav-links">
{links_html}
            </ul>

            <div class="nav-actions">
                <a href="cart.html" class="nav-link"><i class="bi bi-cart3"></i></a>
                <button id="rtl-toggle" class="theme-toggle">
                    <i class="bi bi-translate"></i>
                </button>
                <button id="theme-toggle" class="theme-toggle">
                    <i class="bi bi-sun-fill"></i>
                </button>
                <a href="login.html" class="nav-link d-none d-md-block">Login</a>
                <a href="signup.html" class="btn btn-primary">Sign Up</a>
                <button class="menu-toggle d-lg-none">
                    <i class="bi bi-list"></i>
                </button>
            </div>
        </div>
    </nav>'''

import re

for file_name in html_files:
    if file_name in ['login.html', 'signup.html', '404.html']:
        continue
        
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    active_name = pages.get(file_name, '')
    new_navbar = get_navbar(active_name)
    
    # Replace the existing navbar block
    # This regex tries to find the <nav> block
    content = re.sub(r'<!-- Navbar -->\s*<nav class="navbar">.*?</nav>', new_navbar, content, flags=re.DOTALL)
    # If no comment was found, try replacing just the <nav> block
    if '<nav class="navbar">' in content and new_navbar not in content:
         content = re.sub(r'<nav class="navbar">.*?</nav>', new_navbar, content, flags=re.DOTALL)

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Standardized navbar in {len(html_files)} files.")
