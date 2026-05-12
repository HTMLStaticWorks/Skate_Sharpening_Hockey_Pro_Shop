import os
import re

# The Final Navbar Template (Version 5)
# - RTL button has "RTL" text instead of icon
# - Compact button sizes and refined menu font
REFERENCE_NAVBAR = """    <!-- Navbar -->
    <nav class="navbar">
        <div class="container">
            <a href="index.html" class="nav-logo">
                <i class="bi bi-lightning-charge-fill accent-glow"></i>
                ICEPRO
            </a>

            <ul class="nav-links">
                <li class="dropdown">
                    <a href="#" class="nav-link">Home <i class="bi bi-chevron-down"></i></a>
                    <div class="dropdown-menu">
                        <a href="index.html" class="dropdown-item">Home 1</a>
                        <a href="home-2.html" class="dropdown-item">Home 2</a>
                    </div>
                </li>
                <li><a href="sharpening.html" class="nav-link">Sharpening</a></li>
                <li><a href="customization.html" class="nav-link">Customization</a></li>
                <li><a href="repairs.html" class="nav-link">Repairs</a></li>
                <li><a href="team-orders.html" class="nav-link">Team Orders</a></li>
                <li><a href="shop.html" class="nav-link">Shop</a></li>
                <li><a href="blog.html" class="nav-link">Blog</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>

            <div class="nav-actions">
                <a href="cart.html" class="nav-icon-btn"><i class="bi bi-cart3"></i></a>
                <button id="rtl-toggle" class="theme-toggle" style="font-size: 0.75rem; font-weight: 700;">RTL</button>
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
    </nav>"""

def update_file(file_path):
    if not file_path.endswith('.html'):
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Navbar
    pattern = re.compile(r'<!-- Navbar -->\s*<nav class="navbar">.*?</nav>', re.DOTALL)
    if not pattern.search(content):
        pattern = re.compile(r'<nav class="navbar">.*?</nav>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(REFERENCE_NAVBAR, content)
    else:
        new_content = content

    # 2. Fix the specific 'n>' typo in sharpening.html if present
    if 'sharpening.html' in file_path:
        new_content = new_content.replace('</section>\n n>', '</section>')
        new_content = new_content.replace('</section>\nn>', '</section>')
        new_content = new_content.replace('\n n>\n', '\n')
        new_content = new_content.replace('n>\n\n    <!-- Footer -->', '\n    <!-- Footer -->')

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")
    else:
        print(f"No change or already up to date: {file_path}")

def main():
    root_dir = r"c:\Users\sriva\OneDrive\Desktop\may websites\Skate_Sharpening_Hockey_Pro_Shop"
    for filename in os.listdir(root_dir):
        if filename.endswith(".html"):
            update_file(os.path.join(root_dir, filename))

if __name__ == "__main__":
    main()
