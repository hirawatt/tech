import re
import glob

def fix_cls(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The image still causes CLS. "Media element lacking an explicit size".
    # Wait, the snippet has height="32" and width="107". Why is Lighthouse saying lacking an explicit size?
    # Because of CSS! Let's just add `style="width: 107px; height: 32px;"` or `<style>img[src*='hirawat'] { aspect-ratio: 107/32; }</style>`
    # The bounding rect says width: 107, height: 107. IT RENDERED AS SQUARE!
    # Why? Because we removed `h-8 w-auto` and now the image is behaving differently.
    # Ah! We should put back the class, but fix the width/height to match the aspect ratio of the image file (500x150 -> 10/3 -> ~106.6/32).
    # If the image renders 107x107, it means CSS is making it square or something. Wait, if we use width="107" and height="32", browser sets aspect-ratio. If it renders 107x107, something is wrong with the CSS of its container.
    # Actually, we can just replace the image with width="500" height="150" and keep the original "h-8 w-auto" class. BUT, we MUST have width and height.
    # Wait, the original code had width="500" height="150" AND class="h-8 w-auto". Why did it complain then?
    # Because maybe `w-auto` overrides the aspect ratio calculation? Yes! `height: 2rem` and `width: auto` means the browser cannot calculate the width until the image is loaded.
    # To fix this, we need `aspect-ratio` in CSS or inline style.

    # Let's add `style="aspect-ratio: 500 / 150;"` to all logos.

    content = re.sub(r'(<img[^>]*src="[^"]*hirawat-tech-500-logo.webp"[^>]*)', r'\1 style="aspect-ratio: 500 / 150;"', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in glob.glob('pages/*.html'):
    fix_cls(file)
for file in glob.glob('products/*.html'):
    fix_cls(file)
fix_cls('index.html')
