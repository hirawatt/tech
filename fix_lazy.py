import glob
from bs4 import BeautifulSoup

def fix_lazy(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    # The first logo should probably NOT be lazy loaded as it's LCP (header)
    images = soup.find_all('img')
    if images:
        first_img = images[0]
        if first_img.get('loading') == 'lazy':
            del first_img['loading']
            changed = True
        if first_img.get('decoding') == 'async':
            del first_img['decoding']
            changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed lazy loading in {file_path}")

for file in glob.glob('pages/*.html'):
    fix_lazy(file)
for file in glob.glob('products/*.html'):
    fix_lazy(file)
fix_lazy('index.html')
