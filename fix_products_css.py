import os
import glob

def fix_products_css(file_path, css_file):
    with open(file_path, 'r') as f:
        content = f.read()

    old_css = f'<link rel="stylesheet" href="{css_file}" />'
    new_css = f'<link rel="preload" href="{css_file}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n<noscript><link rel="stylesheet" href="{css_file}"></noscript>'

    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Fixed {file_path}")

fix_products_css('products/piwhatsapp.html', 'main-pi.css')
fix_products_css('products/tryar.html', 'main.css')
