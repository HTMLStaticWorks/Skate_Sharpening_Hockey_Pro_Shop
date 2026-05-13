import os
import re

# Define the directory to search
directory = r'c:\Users\sriva\OneDrive\Desktop\may websites\Skate_Sharpening_Hockey_Pro_Shop'

# Target structure for nav-actions (Desktop view)
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

# Target structure for mobile actions (Inside nav-links)
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
    if not filepath.endswith('.html'):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'class="navbar"' not in content:
        return

    # Cleanup nav-actions: Match the entire div and replace with template
    nav_actions_pattern = re.compile(r'<div class="nav-actions">.*?<button class="menu-toggle d-lg-none">.*?<\/button>.*?<\/div>', re.DOTALL)
    
    # Cleanup nav-links: Remove ANY existing mobile-nav-actions and then add the new one
    # This regex removes any occurrences of the mobile-nav-actions li
    content = re.sub(r'\s*<li class="mobile-nav-actions d-lg-none">.*?</li>', '', content, flags=re.DOTALL)
    
    # Re-find the closing </ul> of nav-links and insert the template
    nav_links_pattern = re.compile(r'(<ul class="nav-links">.*?)(<\/ul>)', re.DOTALL)

    new_content = nav_actions_pattern.sub(desktop_actions_template, content)
    new_content = nav_links_pattern.sub(r'\1' + mobile_actions_template, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned up {filepath}")

for filename in os.listdir(directory):
    update_html_file(os.path.join(directory, filename))
