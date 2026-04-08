import glob
from bs4 import BeautifulSoup

def fix_blocking(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    # Fix CSS links
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if 'font-awesome' in href or 'googleapis.com' in href or 'Material+Icons' in href or 'Inter' in href:
            # Change to preload
            link['rel'] = 'preload'
            link['as'] = 'style'
            link['onload'] = "this.onload=null;this.rel='stylesheet'"

            # Add noscript fallback
            noscript = soup.new_tag('noscript')
            fallback = soup.new_tag('link', rel='stylesheet', href=href)
            noscript.append(fallback)
            link.insert_after(noscript)
            changed = True

    # Fix JS scripts
    for script in soup.find_all('script'):
        if script.get('src') and not script.get('defer') and not script.get('async'):
            script['defer'] = ''
            changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed render blocking in {file_path}")

for file in glob.glob('pages/*.html'):
    fix_blocking(file)
for file in glob.glob('products/*.html'):
    fix_blocking(file)
fix_blocking('index.html')
