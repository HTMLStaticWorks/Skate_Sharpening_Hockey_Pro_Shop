import os
import re

# Define the directory to search
directory = r'c:\Users\sriva\OneDrive\Desktop\may websites\Skate_Sharpening_Hockey_Pro_Shop'

# Target structure for nav-actions (Desktop view) - Login removed
desktop_actions_template = """            <div class="nav-actions">
                <div class="d-none d-lg-flex align-items-center gap-2">
                    <a href="cart.html" class="nav-icon-btn"><i class="bi bi-cart3"></i></a>
                    <button id="rtl-toggle" class="theme-toggle" style="font-size: 0.75rem; font-weight: 700;">RTL</button>
                    <button id="theme-toggle" class="theme-toggle">
                        <i class="bi bi-sun-fill"></i>
                    </button>
                    <a href="signup.html" class="btn btn-primary">Sign Up</a>
                </div>
                <button class="menu-toggle d-lg-none">
                    <i class="bi bi-list"></i>
                </button>
            </div>"""

# Target structure for mobile actions (Inside nav-links) - Login removed
mobile_actions_template = """                <li class="mobile-nav-actions d-lg-none">
                    <div class="mobile-toggle-group">
                        <a href="cart.html" class="nav-icon-btn"><i class="bi bi-cart3"></i></a>
                        <button id="rtl-toggle" class="theme-toggle" style="font-size: 0.75rem; font-weight: 700;">RTL</button>
                        <button id="theme-toggle" class="theme-toggle">
                            <i class="bi bi-sun-fill"></i>
                        </button>
                    </div>
                    <a href="signup.html" class="btn btn-primary w-100">Sign Up</a>
                </li>
            </ul>"""

def update_html_file(filepath):
    # Skip non-html files
    if not filepath.endswith('.html'):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if no navbar
    if 'class="navbar"' not in content:
        return

    # 1. Update nav-actions (Remove login and standardize)
    nav_actions_pattern = re.compile(r'<div class="nav-actions">.*?<button class="menu-toggle d-lg-none">.*?<\/button>.*?<\/div>', re.DOTALL)
    
    # 2. Update nav-links (Remove login and standardize mobile actions)
    # This regex looks for the mobile-nav-actions li if it was already added, or just the end of nav-links
    nav_links_pattern = re.compile(r'(<ul class="nav-links">.*?)(<li class="mobile-nav-actions d-lg-none">.*?<\/li>)?(<\/ul>)', re.DOTALL)

    new_content = nav_actions_pattern.sub(desktop_actions_template, content)
    new_content = nav_links_pattern.sub(r'\1' + mobile_actions_template, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for filename in os.listdir(directory):
    update_html_file(os.path.join(directory, filename))
