import re
import glob
from bs4 import BeautifulSoup

def fix_images(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    for img in soup.find_all('img'):
        # Ensure lazy loading is set for non-hero images (heuristic: if it's below the fold, or if it doesn't already have it)
        # We will add loading="lazy" decoding="async" if not present
        if not img.get('loading'):
            img['loading'] = 'lazy'
            changed = True
        if not img.get('decoding'):
            img['decoding'] = 'async'
            changed = True

        # Try to infer width and height to fix CLS
        # Many images are logos. Let's provide generic safe dimensions or preserve aspect ratio hints
        if not img.get('width') or not img.get('height'):
            # For HirawatTech logo specifically
            if 'hirawat-tech-500-logo.webp' in img.get('src', ''):
                img['width'] = '500'
                img['height'] = '150' # Rough estimate, CSS class="h-8 w-auto" handles scaling
                changed = True
            elif 'unsplash' in img.get('src', ''):
                img['width'] = '1080'
                img['height'] = '720' # Standard unsplash crop
                changed = True

    if changed:
        # Write back but format HTML correctly
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed images in {file_path}")

for file in glob.glob('pages/*.html'):
    fix_images(file)
for file in glob.glob('products/*.html'):
    fix_images(file)
fix_images('index.html')
