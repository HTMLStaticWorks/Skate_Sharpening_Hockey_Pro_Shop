import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

rtl_button = '''                <button id="rtl-toggle" class="theme-toggle">
                    <i class="bi bi-translate"></i>
                </button>'''

rtl_script = '<script src="assets/js/rtl-toggle.js"></script>'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add RTL button
    if 'id="rtl-toggle"' not in content:
        if 'id="theme-toggle"' in content:
            content = content.replace('<button id="theme-toggle"', rtl_button + '\n                <button id="theme-toggle"')
        elif 'class="nav-actions"' in content:
            # Fallback if theme-toggle is missing but nav-actions exists
            content = content.replace('<div class="nav-actions">', '<div class="nav-actions">\n' + rtl_button)
    
    # Add RTL script
    if 'rtl-toggle.js' not in content:
        if 'assets/js/animations.js' in content:
            content = content.replace('<script src="assets/js/animations.js"></script>', rtl_script + '\n    <script src="assets/js/animations.js"></script>')
        elif '</body>' in content:
            content = content.replace('</body>', '    ' + rtl_script + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
