import os
import re

root_dir = r"c:\Users\sriva\OneDrive\Desktop\may websites\Skate_Sharpening_Hockey_Pro_Shop"
favicon_link = '    <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">'

def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Favicon Link if not present
    if 'rel="icon"' not in content:
        # Insert before </head>
        content = content.replace('</head>', f'{favicon_link}\n</head>')

    # 2. Update Navbar Icon
    # Replace <i class="bi bi-lightning-charge-fill accent-glow"></i> 
    # with <i class="bi bi-lightning-charge-fill black-lightning"></i>
    content = content.replace('bi bi-lightning-charge-fill accent-glow', 'bi bi-lightning-charge-fill black-lightning')
    
    # Also handle cases where accent-glow might not be there or slightly different
    # (Just in case)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}")

for filename in os.listdir(root_dir):
    if filename.endswith(".html"):
        update_html(os.path.join(root_dir, filename))
