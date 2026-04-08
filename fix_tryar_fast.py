import re

def fix_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Preload the main css like in index.html (but put it directly inline or inline it if it's so small)
    # The css is 1003 bytes. Let's just inline it!
    # Wait, inlining requires reading the css file.
    css_file = 'products/main.css' if 'tryar' in file_path else 'products/main-pi.css'

    with open(css_file, 'r', encoding='utf-8') as c:
        css = c.read()

    content = re.sub(r'<link rel="stylesheet" href="main(-pi)?\.css" />', f'<style>{css}</style>', content)

    # Also, the iframe loading might be blocking or taking too much LCP time. Let's lazy load the iframe!
    content = content.replace('<iframe height="270px"', '<iframe loading="lazy" height="270px"')

    # LCP is taking 6.9s. The image is likely not optimized. Let's add fetchpriority="high"
    content = content.replace('<img alt="TryAR logo"', '<img fetchpriority="high" alt="TryAR logo"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_html('products/tryar.html')
fix_html('products/piwhatsapp.html')
